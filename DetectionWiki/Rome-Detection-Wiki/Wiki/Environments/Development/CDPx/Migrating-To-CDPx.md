# Migrating a repo from CoreXT to CDPx

These are just main guidelines to be aware of, each repository may have its own additional steps for the migration to succeed successfully.

[[_TOC_]]

## Example PR

[AlertSelector CDPx Migration](https://msazure.visualstudio.com/One/_git/Rome-Detection-AlertSelector/pullrequest/3026548)

## Prerequisite

Although it isn't mandatory, I **highly suggest** you to migrate your tt templates generation to scope bindings before proceeding to this migration.
I found out the hard way that tt isn't fun to migrate to CDPx, especially if that's a Service Fabric Application.

## Setup

1. **Start from a clean local repo (Delete your local repository and re-clone it)**

2. Delete all CoreXT related files
	- .config directory
	- .corext directory
	- build directory
	- all dirs.proj
	- All files located under the main directory (besides owners.txt)
	
4. Add a Nuget.config file to point to the source feeds at the root of your repository. [Sample file](https://dev.azure.com/msazure/One/_git/Rome-Detection-SFMonitoringAgent?path=%2FNuGet.config)

5. Build versioning:
	In case you are going with vanilla msbuild/dotnet code, than there is not auto generated assembly info in local compilation which gets added to each csproj as in CBT/CoreXT, instead the convention is to create a .version folder under the repo root and place a file called PipelineAssemblyInfo.cs in it with the following contents:

	```cs
	// This is a CDP xPlat pipeline generated file
	using System.Reflection;
	[assembly: AssemblyVersion("1.0.0.0")]
	[assembly: AssemblyFileVersion("1.0.0.0")]
	[assembly: AssemblyInformationalVersion ("1.0.0.0-dev-00000000")]
	```
		
	- This is a placeholder file and will be overridden when running a server side build by CDPx.
	- Make sure to link to this file in all of your projects. More info on this stage can be read 
    [here](https://dev.azure.com/onebranch/Pipeline/_wiki/wikis/Pipeline.wiki/313/Repository-Setup), 
    the wiki page for CDPx versioning is 
    [here](https://dev.azure.com/onebranch/Pipeline/_wiki/wikis/Pipeline.wiki/325/Versioning)
		
6. Add **.gitignore** file to the repository. Sample recommended file to start with is this [one](https://dev.azure.com/msazure/One/_git/Rome-Shared-ADF-DatasetPublishActivity?path=%2F.gitignore&version=GBmaster)
	
7. Add **global.json** file to the repository root to enable csproj file with no target SDK (for deployment projects): [file](https://dev.azure.com/msazure/One/_git/Rome-Detection-SFMonitoringAgent?path=%2Fglobal.json)
	
8. Add sample code to the repository under src folder.
	- Note that once you link the version/PipelineAssemblyInfo.cs file to your project, build will fail. To fix that, add the following lines to the csproj:

        ```xml
	    <GenerateAssemblyVersionAttribute>alse<GenerateAssemblyVersionAttribute>

	    <GenerateAssemblyFileVersionAttribte>false<GenerateAssemblyFileVersionAttribue>

	    <GenerateAssemblyInformationalVersonAttribute>false<GenerateAssemblyInformationalVersinAttribute>
        ```

9. In case you have a nuproj, import the following targets file inside:
	$(REPO_ROOT)\RepoTemplate\Targets\SetPackageVersion.targets
		
10. Add Rome-Shared-RepoTemplate as submodule to the repository: 
	- The rome repository template includes common scripts that are used by each of the repositories pipeline yml files, which makes the onboarding to CDPx much easier.
	- Including the repository template as part of your repo should be done by a submodule linked to the **Rome-Shared-RepoTemplate** repository and cloned to the RepoTemplate directory under the repo's root folder.
	- You can do it by running these commands:
	
        ```
    	git submodule add https://dev.azure.com/msazure/One/_git/Rome-Shared-RepoTemplate RepoTemplate
	
    	git submodule update --init --recursive
        ```
		

11. Add the configuration file to onboard to TSA:
	[CDPx TSA wiki](https://dev.azure.com/onebranch/Pipeline/_wiki/wikis/Pipeline.wiki/1074/SDL-Bugfiling-(TSA))
	
    Create a file called .config/tsaoptions.json with the following content:
    ```json
	{
	    "AreaPath": "One\\Rome\\Fundamentals\\SecurityBugs\\TSA",
	    "NotificationAliases": [
	        "RomeDetectionEng@microsoft.com"
	    ]
	}
    ```
	
12. Add pipeline yml file that will orchestrate the build environment. The build is based on docker containers, hence the format of the files and how to run the different steps in the build.

    Example [pipeline.user.windows.yml](https://dev.azure.com/msazure/One/_git/Rome-Shared-ADF-DatasetPublishActivity?path=%2F.pipelines%2Fpipeline.user.windows.yml&version=GBpipelines) file
		
	- By convention all pipeline definition are placed in the .pipelines folder at the root of the repository
	- The file name should be 
    ```
    pipeline.user.<os>.<buildtype>.yml 
    ```
    or
    ```
    pipeline.user.<os>.yml
    ```

    - The values of OS are implicit and can only be linux or windows.
	- The values of Build Type can only be one of official, pullrequest or buddy
	
13. Next thing is to configure a build definition for CDPx in Azure DevOps:
	- Click on Pipeline->OneBranch Pipeline.
	- Select your repository (it might take two times to properly select it).
	- Pick master branch.
	- Pick buddy build for now, later do the same process for pull request and official build types.
    - use CDPX-Windows-Pipelines-1809-D16s-v3 as the image (this might change, occasionally, so confirm).
	- Make sure the checkbox to skip the creation of sample files (pipeline yml) is **checked** - as you already have those files checked in.
		
	You can change build definition after you created it [here](https://onebranchhub-dev.azurewebsites.net/msazure/one/BuildDefinition)


## Create a Solution File

```
Microsoft Visual Studio Solution File, Format Version 12.00
# Visual Studio Version 16
VisualStudioVersion = 16.0.29911.84
MinimumVisualStudioVersion = 10.0.40219.1
Global
	GlobalSection(SolutionConfigurationPlatforms) = preSolution
		Debug|Any CPU = Debug|Any CPU
		Debug|x64 = Debug|x64
		Release|Any CPU = Release|Any CPU
		Release|x64 = Release|x64
	EndGlobalSection
	GlobalSection(ProjectConfigurationPlatforms) = postSolution
	EndGlobalSection
	GlobalSection(SolutionProperties) = preSolution
		HideSolutionNode = FALSE
	EndGlobalSection
	GlobalSection(ExtensibilityGlobals) = postSolution
		SolutionGuid = {18F2461B-C2A7-4E40-A749-B73FB90F372F}
	EndGlobalSection
EndGlobal
```

## Building Locally

Now we'll work on successfully building the project locally,
We'll go a project after another and adjust it to be built without CoreXT dependencies and imports.
Start with the project which is the first in the build dependencies (e.g. Infra proj in some repos).

1. I found that creating new csproj is easier than altering an existing one, so start from (Change the relevant fields):

	```xml
	<?xml version="1.0" encoding="utf-8"?>
	<Project Sdk="Microsoft.NET.Sdk">

	<PropertyGroup>
		<TargetFramework>net472</TargetFramework>
		<AssemblyName>Microsoft.Azure.Security.Detection.AlertSelector.EventHubConsumer</AssemblyName>
		<RootNamespace>Microsoft.Azure.Security.Detection.AlertSelector.EventHubConsumer</RootNamespace>
		<ProjectGuid>{4DED1806-C056-4D61-90EC-3779DB1AA209}</ProjectGuid>
		<GenerateAssemblyVersionAttribute>false</GenerateAssemblyVersionAttribute>
		<GenerateAssemblyFileVersionAttribute>false</GenerateAssemblyFileVersionAttribute>
		<GenerateAssemblyInformationalVersionAttribute>false</GenerateAssemblyInformationalVersionAttribute>
		<ResolveAssemblyWarnOrErrorOnTargetArchitectureMismatch>None</ResolveAssemblyWarnOrErrorOnTargetArchitectureMismatch>
	</PropertyGroup>

	<ItemGroup>
		<Compile Include="..\..\.version\PipelineAssemblyInfo.cs" Link="Properties\PipelineAssemblyInfo.cs" />
	</ItemGroup>
	
	<ItemGroup>
		<Reference Include="System" />
		<Reference Include="System.Core" />
		<Reference Include="System.Drawing" />
		<Reference Include="System.IdentityModel" />
		<Reference Include="System.Net" />
		<Reference Include="System.Runtime.Serialization" />
		<Reference Include="System.ServiceModel" />
		<Reference Include="System.Threading.Tasks" />
		<Reference Include="System.IO.Compression" />
		<Reference Include="System.Transactions" />
		<Reference Include="System.Web" />
		<Reference Include="System.Windows.Forms" />
		<Reference Include="System.Xml" />
		<Reference Include="System.Xml.Linq" />
	</ItemGroup>
	
	</Project>
	```

	Make sure to substitutes all the core references with the ones existed in your csproj.

2. Edit the sln file to include the new project:

	```sln
	Microsoft Visual Studio Solution File, Format Version 12.00
	# Visual Studio Version 16
	VisualStudioVersion = 16.0.29911.84
	MinimumVisualStudioVersion = 10.0.40219.1
	Project("{9A19103F-16F7-4668-BE54-9A1E7A4F7556}") = "Infra", "src\Infra\Infra.csproj", "{BD1B1974-A018-4283-B765-B783F5646CC3}"
	EndProject
	Global
		GlobalSection(SolutionConfigurationPlatforms) = preSolution
			Debug|Any CPU = Debug|Any CPU
			Debug|x64 = Debug|x64
			Release|Any CPU = Release|Any CPU
			Release|x64 = Release|x64
		EndGlobalSection
		GlobalSection(ProjectConfigurationPlatforms) = postSolution
			{BD1B1974-A018-4283-B765-B783F5646CC3}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
			{BD1B1974-A018-4283-B765-B783F5646CC3}.Debug|Any CPU.Build.0 = Debug|Any CPU
			{BD1B1974-A018-4283-B765-B783F5646CC3}.Debug|x64.ActiveCfg = Debug|Any CPU
			{BD1B1974-A018-4283-B765-B783F5646CC3}.Debug|x64.Build.0 = Debug|Any CPU
			{BD1B1974-A018-4283-B765-B783F5646CC3}.Release|Any CPU.ActiveCfg = Release|Any CPU
			{BD1B1974-A018-4283-B765-B783F5646CC3}.Release|Any CPU.Build.0 = Release|Any CPU
			{BD1B1974-A018-4283-B765-B783F5646CC3}.Release|x64.ActiveCfg = Release|Any CPU
			{BD1B1974-A018-4283-B765-B783F5646CC3}.Release|x64.Build.0 = Release|Any CPU
		EndGlobalSection
		GlobalSection(SolutionProperties) = preSolution
			HideSolutionNode = FALSE
		EndGlobalSection
		GlobalSection(ExtensibilityGlobals) = postSolution
			SolutionGuid = {18F2461B-C2A7-4E40-A749-B73FB90F372F}
		EndGlobalSection
	EndGlobal
	```

3. Add the relevant project dependencies.

4. Download the required Nugets:
	- Open the sln file using Visual Studio 2019. You should now get tons of compiling errors due to missing Nugets.
	- Now there are 2 ways to import nugets. You can either use Nuget.config (BAD) or use PackageReference inside the csproj.
	- Basically Nuget.config enforces you to manually specify all the nugets you want and their **dependencies** and their dependencies' dependencies (and so on), i.e. if lets say I want to install AlertContracts Nuget, I will also have to specify the Newtsoft json nuget which is being used by the first.
	- This is obviously terrible and hence, PackageReference is the right way to go (takes care of each of the nugets' dependencies)
	- Start by going through the using errors and identify the missing nugets by looking at the using statements at the top of each cs file.
		- for example: If I see:
		```cs
			using Microsoft.Azure.Security.Instrumentation;
		```
		- I probably need Microsoft.Azure.Security.Detection.Ifx nuget. I'll look for that nuget in the nuget.config file and see its version, then I'll go to the VS Nuget Package Manager and download the same version for this project. This will automatically add to the csproj something like
		```xml
			<PackageReference Include="Microsoft.Azure.Security.Instrumentation" Version="2.0.1.7" />
		```

5. EmbeddedResources: 
Don't forget to add all of the embedded resources listed in the old csproj. E.g.
```xml
    <EmbeddedResource Include="Configurations\FiltersTopology.json" />
```

After you complete all of the steps above for each of the projects + test projects, Build everything and run the tests.

## Packaging
While up until now everything was a bit straight forward, this part is a bit tricky.
Packaging occurs in various places such as Service Fabric Applications / Nugets etc...
CDPx will **not** sign files inside a package, hence, we need to perform some manipulations in order to make it do so.

What we need to do is to separate the building and the packaging into different CDPx build steps.
```xml
  <Target Name="Package">
    <ItemGroup>
      <AlertSelectorApp Include="..\AlertSelectorApp\pkg\$(Configuration)\**" />
    </ItemGroup>
    <Zip ZipFileName="$(OutDir)\ServiceGroupRoot\bin\AlertSelectorApp.sfpkg" Files="@(AlertSelectorApp)" WorkingDirectory="..\AlertSelectorApp\pkg\$(Configuration)" />
  </Target>
```

Notice that there is no AfterTargets in the Target definition, hence, it will not run on a normal build as it is not part of the build tree.
This will only be trigger on a later CDPx build step by following this definition in the pipeline yml (notice the /t flag):
```yml
package:
  commands:
    - !!buildcommand
      name: 'Zip Service Fabric Package'
      command: 'RepoTemplate\build\cs\msbuild2019.cmd'
      arguments: '/p:Configuration=Release /t:Package src\Deployment\Deployment.csproj'
      logs:
        - to: 'Build Logs'
          include:
            - '**/build.log'
      artifacts:
        - from: 'src'
          to: 'output'
          include:
            - '**/bin/release/**/*'
```

## Service Fabric Versioning

Add the following to your sfproj:
```xml
  <Target Name="UpdateBuildVersion" AfterTargets="Package">
    <PropertyGroup>
      <CDP_PACKAGE_VERSION_NUMERIC Condition=" '$(CDP_PACKAGE_VERSION_NUMERIC)' == '' ">1.0.0_$([System.DateTime]::Now.ToString("yyyy.MM.dd_HH"))</CDP_PACKAGE_VERSION_NUMERIC>
    </PropertyGroup>
    <ItemGroup>
      <ManifestRootDir Include="$(PackageLocation)\" />
    </ItemGroup>
    <Message Text="Updating Manifests with build version: $(CDP_PACKAGE_VERSION_NUMERIC)" Importance="high" />
    <Exec Command="powershell.exe -ExecutionPolicy Bypass -NoProfile -Command &quot; $(ProjectDir)..\..\RepoTemplate\Versioning\Update-BuildVersion.ps1 -DirToUpdate @(ManifestRootDir) -Pattern '*Manifest.xml' -TargetVersion '$(CDP_PACKAGE_VERSION_NUMERIC)' &quot;" />
  </Target>
```

Add these lines to your Deployment proj (change the AfterTargets accordingly):
```xml
  <Target Name="UpdateBuildVersion" AfterTargets="CopyFiles">
    <ItemGroup>
      <ParameterFiles Include="$(OutDir)\ServiceGroupRoot\Parameters\**" />
    </ItemGroup>
    <PropertyGroup>
      <CDP_PACKAGE_VERSION_NUMERIC Condition=" '$(CDP_PACKAGE_VERSION_NUMERIC)' == '' ">1.0.0_$([System.DateTime]::Now.ToString("yyyy.MM.dd_HH"))</CDP_PACKAGE_VERSION_NUMERIC>
    </PropertyGroup>
    <Message Text="Updating Manifests with $(CDP_PACKAGE_VERSION_NUMERIC)" />
    <FileUpdate Files="@(ParameterFiles)" Regex="\[BuildVersion\]" ReplacementText="$(CDP_PACKAGE_VERSION_NUMERIC)" />
    <Exec Command="echo $(CDP_PACKAGE_VERSION_NUMERIC) &gt; $(OutDir)\ServiceGroupRoot\buildver.txt" />
  </Target>
```