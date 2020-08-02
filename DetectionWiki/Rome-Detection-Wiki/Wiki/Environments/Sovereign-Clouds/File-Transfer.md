In case you need any custom tool or script in any sovereign cloud, you need to copy it to there somehow.
Assuming you can't copy-paste it there (in case the tool is not plain text) or you don't have access at all (EX env for example), you'll need to use replication-only release defintion.

Here is the explaination how to do that: [General](https://onebranch.visualstudio.com/onebranch/_wiki/wikis/OneBranch.wiki/1885/Replication-Only-Release-Definition), [LX](https://onebranch.visualstudio.com/onebranch/_wiki/wikis/OneBranch.wiki/1268/Replication-Only-Release-Definition-(LX))

Lucky you, we've already impelemnted a centralized place for such tasks:

1. Push you changes to [Rome-Detection-Toolset](https://dev.azure.com/msazure/One/_git/Rome-Detection-Toolset) repo (using pull-request)
2. Once pushed, run [official build on the repo](https://dev.azure.com/msazure/One/_build?definitionId=128851&_a=summary). In case this link is brokwn, you can find the relevant pipeline in [this](https://dev.azure.com/msazure/One/_build?view=folders&pipelineNameFilter=Rome-Detection) list (just scroll down)
3. Once official build done, run [this](https://dev.azure.com/msazure/One/_release?definitionId=17818&_a=releases&view=mine) release.
4. Once done, your files will be available in the required cloud, under:

| Cloud Environment | Path |
|-----------|-----------|
| Fairfax | \\\USOE.GBL\Public\builds\branches\rome_detection_toolset_master |
| Mooncake | \\\CAZ.GBL\builds\branches\rome_detection_toolset_master |
| UsNat | \\\EXME.GBL.EAGLEX.IC.GOV\SERVICES\USNAT\WARM\Builds\rome_detection_toolset_master |
| UsSec | \\\RXME.GBL.MICROSOFT.SCLOUD\Services\USSec\WARM\Builds\rome_detection_toolset_master |