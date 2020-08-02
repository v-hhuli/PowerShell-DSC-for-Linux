/* @migen@ */
#include "MSFT_nxOMSSyslogResource.h"


#include "debug_tags.hpp"
#include "MI.h"
#include "PythonProvider.hpp"


#include <cstdlib>


typedef struct _MSFT_nxOMSSyslogResource_Self : public scx::PythonProvider
{
    /*ctor*/ _MSFT_nxOMSSyslogResource_Self ()
        : scx::PythonProvider ("nxOMSSyslog")
    {
        // empty
    }
} MSFT_nxOMSSyslogResource_Self;


void MI_CALL MSFT_nxOMSSyslogResource_Load(
    _Outptr_result_maybenull_ MSFT_nxOMSSyslogResource_Self** self,
    _In_opt_ MI_Module_Self* selfModule,
    _In_ MI_Context* context)
{
    SCX_BOOKEND_EX ("Load", " name=\"nxOMSSyslog\"");
    MI_UNREFERENCED_PARAMETER(selfModule);
    MI_Result res = MI_RESULT_OK;
    if (0 != self)
    {
        if (0 == *self)
        {
            *self = new MSFT_nxOMSSyslogResource_Self;
            if (EXIT_SUCCESS != (*self)->init ())
            {
                delete *self;
                *self = 0;
                res = MI_RESULT_FAILED;
            }
        }
    }
    else
    {
        res = MI_RESULT_FAILED;
    }
    MI_Context_PostResult(context, res);
}

void MI_CALL MSFT_nxOMSSyslogResource_Unload(
    _In_opt_ MSFT_nxOMSSyslogResource_Self* self,
    _In_ MI_Context* context)
{
    SCX_BOOKEND_EX ("Unload", " name=\"nxOMSSyslog\"");
    if (self)
    {
        delete self;
    }
    MI_Context_PostResult(context, MI_RESULT_OK);
}

void MI_CALL MSFT_nxOMSSyslogResource_EnumerateInstances(
    _In_opt_ MSFT_nxOMSSyslogResource_Self* self,
    _In_ MI_Context* context,
    _In_opt_z_ const MI_Char* nameSpace,
    _In_opt_z_ const MI_Char* className,
    _In_opt_ const MI_PropertySet* propertySet,
    _In_ MI_Boolean keysOnly,
    _In_opt_ const MI_Filter* filter)
{
    MI_UNREFERENCED_PARAMETER(self);
    MI_UNREFERENCED_PARAMETER(nameSpace);
    MI_UNREFERENCED_PARAMETER(className);
    MI_UNREFERENCED_PARAMETER(propertySet);
    MI_UNREFERENCED_PARAMETER(keysOnly);
    MI_UNREFERENCED_PARAMETER(filter);

    MI_Context_PostResult(context, MI_RESULT_NOT_SUPPORTED);
}

void MI_CALL MSFT_nxOMSSyslogResource_GetInstance(
    _In_opt_ MSFT_nxOMSSyslogResource_Self* self,
    _In_ MI_Context* context,
    _In_opt_z_ const MI_Char* nameSpace,
    _In_opt_z_ const MI_Char* className,
    _In_ const MSFT_nxOMSSyslogResource* instanceName,
    _In_opt_ const MI_PropertySet* propertySet)
{
    MI_UNREFERENCED_PARAMETER(self);
    MI_UNREFERENCED_PARAMETER(nameSpace);
    MI_UNREFERENCED_PARAMETER(className);
    MI_UNREFERENCED_PARAMETER(instanceName);
    MI_UNREFERENCED_PARAMETER(propertySet);

    MI_Context_PostResult(context, MI_RESULT_NOT_SUPPORTED);
}

void MI_CALL MSFT_nxOMSSyslogResource_CreateInstance(
    _In_opt_ MSFT_nxOMSSyslogResource_Self* self,
    _In_ MI_Context* context,
    _In_opt_z_ const MI_Char* nameSpace,
    _In_opt_z_ const MI_Char* className,
    _In_ const MSFT_nxOMSSyslogResource* newInstance)
{
    MI_UNREFERENCED_PARAMETER(self);
    MI_UNREFERENCED_PARAMETER(nameSpace);
    MI_UNREFERENCED_PARAMETER(className);
    MI_UNREFERENCED_PARAMETER(newInstance);

    MI_Context_PostResult(context, MI_RESULT_NOT_SUPPORTED);
}

void MI_CALL MSFT_nxOMSSyslogResource_ModifyInstance(
    _In_opt_ MSFT_nxOMSSyslogResource_Self* self,
    _In_ MI_Context* context,
    _In_opt_z_ const MI_Char* nameSpace,
    _In_opt_z_ const MI_Char* className,
    _In_ const MSFT_nxOMSSyslogResource* modifiedInstance,
    _In_opt_ const MI_PropertySet* propertySet)
{
    MI_UNREFERENCED_PARAMETER(self);
    MI_UNREFERENCED_PARAMETER(nameSpace);
    MI_UNREFERENCED_PARAMETER(className);
    MI_UNREFERENCED_PARAMETER(modifiedInstance);
    MI_UNREFERENCED_PARAMETER(propertySet);

    MI_Context_PostResult(context, MI_RESULT_NOT_SUPPORTED);
}

void MI_CALL MSFT_nxOMSSyslogResource_DeleteInstance(
    _In_opt_ MSFT_nxOMSSyslogResource_Self* self,
    _In_ MI_Context* context,
    _In_opt_z_ const MI_Char* nameSpace,
    _In_opt_z_ const MI_Char* className,
    _In_ const MSFT_nxOMSSyslogResource* instanceName)
{
    MI_UNREFERENCED_PARAMETER(self);
    MI_UNREFERENCED_PARAMETER(nameSpace);
    MI_UNREFERENCED_PARAMETER(className);
    MI_UNREFERENCED_PARAMETER(instanceName);

    MI_Context_PostResult(context, MI_RESULT_NOT_SUPPORTED);
}

void MI_CALL MSFT_nxOMSSyslogResource_Invoke_GetTargetResource(
    _In_opt_ MSFT_nxOMSSyslogResource_Self* self,
    _In_ MI_Context* context,
    _In_opt_z_ const MI_Char* nameSpace,
    _In_opt_z_ const MI_Char* className,
    _In_opt_z_ const MI_Char* methodName,
    _In_ const MSFT_nxOMSSyslogResource* instanceName,
    _In_opt_ const MSFT_nxOMSSyslogResource_GetTargetResource* in)
{
    SCX_BOOKEND_EX ("Get", " name=\"nxOMSSyslog\"");
    MI_Result result = MI_RESULT_FAILED;
    if (self)
    {
        MI_Instance* retInstance;
        MI_Instance_Clone (&in->InputResource.value->__instance, &retInstance);
        result = self->get (in->InputResource.value->__instance, context,
                            retInstance);
        if (MI_RESULT_OK == result)
        {
            SCX_BOOKEND_PRINT ("packing succeeded!");
            MSFT_nxOMSSyslogResource_GetTargetResource out;
            MSFT_nxOMSSyslogResource_GetTargetResource_Construct (&out, context);
            MSFT_nxOMSSyslogResource_GetTargetResource_Set_MIReturn (&out, 0);
            MI_Value value;
            value.instance = retInstance;
            MI_Instance_SetElement (&out.__instance, "OutputResource", &value,
                                    MI_INSTANCE, 0);
            result = MSFT_nxOMSSyslogResource_GetTargetResource_Post (&out, context);
            if (MI_RESULT_OK != result)
            {
                SCX_BOOKEND_PRINT ("post Failed");
            }
            MSFT_nxOMSSyslogResource_GetTargetResource_Destruct (&out);
        }
        else
        {
            SCX_BOOKEND_PRINT ("get FAILED");
        }
        MI_Instance_Delete (retInstance);
    }
    MI_Context_PostResult (context, result);
}

void MI_CALL MSFT_nxOMSSyslogResource_Invoke_TestTargetResource(
    _In_opt_ MSFT_nxOMSSyslogResource_Self* self,
    _In_ MI_Context* context,
    _In_opt_z_ const MI_Char* nameSpace,
    _In_opt_z_ const MI_Char* className,
    _In_opt_z_ const MI_Char* methodName,
    _In_ const MSFT_nxOMSSyslogResource* instanceName,
    _In_opt_ const MSFT_nxOMSSyslogResource_TestTargetResource* in)
{
    MI_Result result = MI_RESULT_FAILED;
    if (self)
    {
        MI_Boolean testResult = MI_FALSE;
        result = self->test (in->InputResource.value->__instance, &testResult);
        if (MI_RESULT_OK == result)
        {
            MSFT_nxOMSSyslogResource_TestTargetResource out;
            MSFT_nxOMSSyslogResource_TestTargetResource_Construct (&out, context);
            MSFT_nxOMSSyslogResource_TestTargetResource_Set_Result (
                &out, testResult);
            MSFT_nxOMSSyslogResource_TestTargetResource_Set_MIReturn (&out, 0);
            MSFT_nxOMSSyslogResource_TestTargetResource_Post (&out, context);
            MSFT_nxOMSSyslogResource_TestTargetResource_Destruct (&out);
        }
    }
    MI_Context_PostResult (context, result);
}

void MI_CALL MSFT_nxOMSSyslogResource_Invoke_SetTargetResource(
    _In_opt_ MSFT_nxOMSSyslogResource_Self* self,
    _In_ MI_Context* context,
    _In_opt_z_ const MI_Char* nameSpace,
    _In_opt_z_ const MI_Char* className,
    _In_opt_z_ const MI_Char* methodName,
    _In_ const MSFT_nxOMSSyslogResource* instanceName,
    _In_opt_ const MSFT_nxOMSSyslogResource_SetTargetResource* in)
{
    MI_Result result = MI_RESULT_FAILED;
    if (self)
    {
        MI_Result setResult = MI_RESULT_FAILED;
        result = self->set (in->InputResource.value->__instance, &setResult);
        if (MI_RESULT_OK == result)
        {
            result = setResult;
            MSFT_nxOMSSyslogResource_SetTargetResource out;
            MSFT_nxOMSSyslogResource_SetTargetResource_Construct (&out, context);
            MSFT_nxOMSSyslogResource_SetTargetResource_Set_MIReturn (
                &out, setResult);
            MSFT_nxOMSSyslogResource_SetTargetResource_Post (&out, context);
            MSFT_nxOMSSyslogResource_SetTargetResource_Destruct (&out);
        }
    }
    MI_Context_PostResult (context, result);
}
