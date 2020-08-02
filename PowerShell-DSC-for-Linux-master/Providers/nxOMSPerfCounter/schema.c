/* @migen@ */
/*
**==============================================================================
**
** WARNING: THIS FILE WAS AUTOMATICALLY GENERATED. PLEASE DO NOT EDIT.
**
**==============================================================================
*/
#include <ctype.h>
#include <MI.h>
#include "MSFT_nxOMSPerfCounterResource.h"

/*
**==============================================================================
**
** Schema Declaration
**
**==============================================================================
*/

MI_EXTERN_C MI_SchemaDecl schemaDecl;

/*
**==============================================================================
**
** Qualifier declarations
**
**==============================================================================
*/

static MI_CONST MI_Boolean Abstract_qual_decl_value = 0;

static MI_CONST MI_QualifierDecl Abstract_qual_decl =
{
    MI_T("Abstract"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_ASSOCIATION|MI_FLAG_CLASS|MI_FLAG_INDICATION, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_RESTRICTED, /* flavor */
    0, /* subscript */
    &Abstract_qual_decl_value, /* value */
};

static MI_CONST MI_Boolean Aggregate_qual_decl_value = 0;

static MI_CONST MI_QualifierDecl Aggregate_qual_decl =
{
    MI_T("Aggregate"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_REFERENCE, /* scope */
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &Aggregate_qual_decl_value, /* value */
};

static MI_CONST MI_Boolean Aggregation_qual_decl_value = 0;

static MI_CONST MI_QualifierDecl Aggregation_qual_decl =
{
    MI_T("Aggregation"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_ASSOCIATION, /* scope */
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &Aggregation_qual_decl_value, /* value */
};

static MI_CONST MI_Char* ArrayType_qual_decl_value = MI_T("Bag");

static MI_CONST MI_QualifierDecl ArrayType_qual_decl =
{
    MI_T("ArrayType"), /* name */
    MI_STRING, /* type */
    MI_FLAG_PARAMETER|MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &ArrayType_qual_decl_value, /* value */
};

static MI_CONST MI_Boolean Association_qual_decl_value = 0;

static MI_CONST MI_QualifierDecl Association_qual_decl =
{
    MI_T("Association"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_ASSOCIATION, /* scope */
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &Association_qual_decl_value, /* value */
};

static MI_CONST MI_QualifierDecl BitMap_qual_decl =
{
    MI_T("BitMap"), /* name */
    MI_STRINGA, /* type */
    MI_FLAG_METHOD|MI_FLAG_PARAMETER|MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_QualifierDecl BitValues_qual_decl =
{
    MI_T("BitValues"), /* name */
    MI_STRINGA, /* type */
    MI_FLAG_METHOD|MI_FLAG_PARAMETER|MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_QualifierDecl ClassConstraint_qual_decl =
{
    MI_T("ClassConstraint"), /* name */
    MI_STRINGA, /* type */
    MI_FLAG_ASSOCIATION|MI_FLAG_CLASS|MI_FLAG_INDICATION, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_QualifierDecl ClassVersion_qual_decl =
{
    MI_T("ClassVersion"), /* name */
    MI_STRING, /* type */
    MI_FLAG_ASSOCIATION|MI_FLAG_CLASS|MI_FLAG_INDICATION, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_RESTRICTED, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_Boolean Composition_qual_decl_value = 0;

static MI_CONST MI_QualifierDecl Composition_qual_decl =
{
    MI_T("Composition"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_ASSOCIATION, /* scope */
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &Composition_qual_decl_value, /* value */
};

static MI_CONST MI_QualifierDecl Correlatable_qual_decl =
{
    MI_T("Correlatable"), /* name */
    MI_STRINGA, /* type */
    MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_Boolean Counter_qual_decl_value = 0;

static MI_CONST MI_QualifierDecl Counter_qual_decl =
{
    MI_T("Counter"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_METHOD|MI_FLAG_PARAMETER|MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &Counter_qual_decl_value, /* value */
};

static MI_CONST MI_QualifierDecl Deprecated_qual_decl =
{
    MI_T("Deprecated"), /* name */
    MI_STRINGA, /* type */
    MI_FLAG_ANY, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_RESTRICTED, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_QualifierDecl Description_qual_decl =
{
    MI_T("Description"), /* name */
    MI_STRING, /* type */
    MI_FLAG_ANY, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_QualifierDecl DisplayName_qual_decl =
{
    MI_T("DisplayName"), /* name */
    MI_STRING, /* type */
    MI_FLAG_ANY, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_Boolean DN_qual_decl_value = 0;

static MI_CONST MI_QualifierDecl DN_qual_decl =
{
    MI_T("DN"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_METHOD|MI_FLAG_PARAMETER|MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &DN_qual_decl_value, /* value */
};

static MI_CONST MI_QualifierDecl EmbeddedInstance_qual_decl =
{
    MI_T("EmbeddedInstance"), /* name */
    MI_STRING, /* type */
    MI_FLAG_METHOD|MI_FLAG_PARAMETER|MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_Boolean EmbeddedObject_qual_decl_value = 0;

static MI_CONST MI_QualifierDecl EmbeddedObject_qual_decl =
{
    MI_T("EmbeddedObject"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_METHOD|MI_FLAG_PARAMETER|MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &EmbeddedObject_qual_decl_value, /* value */
};

static MI_CONST MI_Boolean Exception_qual_decl_value = 0;

static MI_CONST MI_QualifierDecl Exception_qual_decl =
{
    MI_T("Exception"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_CLASS|MI_FLAG_INDICATION, /* scope */
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &Exception_qual_decl_value, /* value */
};

static MI_CONST MI_Boolean Experimental_qual_decl_value = 0;

static MI_CONST MI_QualifierDecl Experimental_qual_decl =
{
    MI_T("Experimental"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_ANY, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_RESTRICTED, /* flavor */
    0, /* subscript */
    &Experimental_qual_decl_value, /* value */
};

static MI_CONST MI_Boolean Gauge_qual_decl_value = 0;

static MI_CONST MI_QualifierDecl Gauge_qual_decl =
{
    MI_T("Gauge"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_METHOD|MI_FLAG_PARAMETER|MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &Gauge_qual_decl_value, /* value */
};

static MI_CONST MI_Boolean In_qual_decl_value = 1;

static MI_CONST MI_QualifierDecl In_qual_decl =
{
    MI_T("In"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_PARAMETER, /* scope */
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &In_qual_decl_value, /* value */
};

static MI_CONST MI_Boolean Indication_qual_decl_value = 0;

static MI_CONST MI_QualifierDecl Indication_qual_decl =
{
    MI_T("Indication"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_CLASS|MI_FLAG_INDICATION, /* scope */
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &Indication_qual_decl_value, /* value */
};

static MI_CONST MI_Boolean IsPUnit_qual_decl_value = 0;

static MI_CONST MI_QualifierDecl IsPUnit_qual_decl =
{
    MI_T("IsPUnit"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_METHOD|MI_FLAG_PARAMETER|MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &IsPUnit_qual_decl_value, /* value */
};

static MI_CONST MI_Boolean Key_qual_decl_value = 0;

static MI_CONST MI_QualifierDecl Key_qual_decl =
{
    MI_T("Key"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_PROPERTY|MI_FLAG_REFERENCE, /* scope */
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &Key_qual_decl_value, /* value */
};

static MI_CONST MI_QualifierDecl MappingStrings_qual_decl =
{
    MI_T("MappingStrings"), /* name */
    MI_STRINGA, /* type */
    MI_FLAG_ANY, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_QualifierDecl Max_qual_decl =
{
    MI_T("Max"), /* name */
    MI_UINT32, /* type */
    MI_FLAG_REFERENCE, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_QualifierDecl MaxLen_qual_decl =
{
    MI_T("MaxLen"), /* name */
    MI_UINT32, /* type */
    MI_FLAG_METHOD|MI_FLAG_PARAMETER|MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_QualifierDecl MaxValue_qual_decl =
{
    MI_T("MaxValue"), /* name */
    MI_SINT64, /* type */
    MI_FLAG_METHOD|MI_FLAG_PARAMETER|MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_QualifierDecl MethodConstraint_qual_decl =
{
    MI_T("MethodConstraint"), /* name */
    MI_STRINGA, /* type */
    MI_FLAG_METHOD, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_Uint32 Min_qual_decl_value = 0U;

static MI_CONST MI_QualifierDecl Min_qual_decl =
{
    MI_T("Min"), /* name */
    MI_UINT32, /* type */
    MI_FLAG_REFERENCE, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &Min_qual_decl_value, /* value */
};

static MI_CONST MI_Uint32 MinLen_qual_decl_value = 0U;

static MI_CONST MI_QualifierDecl MinLen_qual_decl =
{
    MI_T("MinLen"), /* name */
    MI_UINT32, /* type */
    MI_FLAG_METHOD|MI_FLAG_PARAMETER|MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &MinLen_qual_decl_value, /* value */
};

static MI_CONST MI_QualifierDecl MinValue_qual_decl =
{
    MI_T("MinValue"), /* name */
    MI_SINT64, /* type */
    MI_FLAG_METHOD|MI_FLAG_PARAMETER|MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_QualifierDecl ModelCorrespondence_qual_decl =
{
    MI_T("ModelCorrespondence"), /* name */
    MI_STRINGA, /* type */
    MI_FLAG_ANY, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_QualifierDecl Nonlocal_qual_decl =
{
    MI_T("Nonlocal"), /* name */
    MI_STRING, /* type */
    MI_FLAG_REFERENCE, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_QualifierDecl NonlocalType_qual_decl =
{
    MI_T("NonlocalType"), /* name */
    MI_STRING, /* type */
    MI_FLAG_REFERENCE, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_QualifierDecl NullValue_qual_decl =
{
    MI_T("NullValue"), /* name */
    MI_STRING, /* type */
    MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_Boolean Octetstring_qual_decl_value = 0;

static MI_CONST MI_QualifierDecl Octetstring_qual_decl =
{
    MI_T("Octetstring"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_METHOD|MI_FLAG_PARAMETER|MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &Octetstring_qual_decl_value, /* value */
};

static MI_CONST MI_Boolean Out_qual_decl_value = 0;

static MI_CONST MI_QualifierDecl Out_qual_decl =
{
    MI_T("Out"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_PARAMETER, /* scope */
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &Out_qual_decl_value, /* value */
};

static MI_CONST MI_QualifierDecl Override_qual_decl =
{
    MI_T("Override"), /* name */
    MI_STRING, /* type */
    MI_FLAG_METHOD|MI_FLAG_PROPERTY|MI_FLAG_REFERENCE, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_RESTRICTED, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_QualifierDecl Propagated_qual_decl =
{
    MI_T("Propagated"), /* name */
    MI_STRING, /* type */
    MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_QualifierDecl PropertyConstraint_qual_decl =
{
    MI_T("PropertyConstraint"), /* name */
    MI_STRINGA, /* type */
    MI_FLAG_PROPERTY|MI_FLAG_REFERENCE, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_QualifierDecl PUnit_qual_decl =
{
    MI_T("PUnit"), /* name */
    MI_STRING, /* type */
    MI_FLAG_METHOD|MI_FLAG_PARAMETER|MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_Boolean Read_qual_decl_value = 1;

static MI_CONST MI_QualifierDecl Read_qual_decl =
{
    MI_T("Read"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &Read_qual_decl_value, /* value */
};

static MI_CONST MI_Boolean Required_qual_decl_value = 0;

static MI_CONST MI_QualifierDecl Required_qual_decl =
{
    MI_T("Required"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_METHOD|MI_FLAG_PARAMETER|MI_FLAG_PROPERTY|MI_FLAG_REFERENCE, /* scope */
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &Required_qual_decl_value, /* value */
};

static MI_CONST MI_QualifierDecl Revision_qual_decl =
{
    MI_T("Revision"), /* name */
    MI_STRING, /* type */
    MI_FLAG_ASSOCIATION|MI_FLAG_CLASS|MI_FLAG_INDICATION, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_QualifierDecl Schema_qual_decl =
{
    MI_T("Schema"), /* name */
    MI_STRING, /* type */
    MI_FLAG_METHOD|MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_QualifierDecl Source_qual_decl =
{
    MI_T("Source"), /* name */
    MI_STRING, /* type */
    MI_FLAG_ASSOCIATION|MI_FLAG_CLASS|MI_FLAG_INDICATION, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_QualifierDecl SourceType_qual_decl =
{
    MI_T("SourceType"), /* name */
    MI_STRING, /* type */
    MI_FLAG_ASSOCIATION|MI_FLAG_CLASS|MI_FLAG_INDICATION|MI_FLAG_REFERENCE, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_Boolean Static_qual_decl_value = 0;

static MI_CONST MI_QualifierDecl Static_qual_decl =
{
    MI_T("Static"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_METHOD|MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &Static_qual_decl_value, /* value */
};

static MI_CONST MI_Boolean Stream_qual_decl_value = 0;

static MI_CONST MI_QualifierDecl Stream_qual_decl =
{
    MI_T("Stream"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_METHOD|MI_FLAG_PARAMETER, /* scope */
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &Stream_qual_decl_value, /* value */
};

static MI_CONST MI_Boolean Terminal_qual_decl_value = 0;

static MI_CONST MI_QualifierDecl Terminal_qual_decl =
{
    MI_T("Terminal"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_ASSOCIATION|MI_FLAG_CLASS|MI_FLAG_INDICATION, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &Terminal_qual_decl_value, /* value */
};

static MI_CONST MI_QualifierDecl UMLPackagePath_qual_decl =
{
    MI_T("UMLPackagePath"), /* name */
    MI_STRING, /* type */
    MI_FLAG_ASSOCIATION|MI_FLAG_CLASS|MI_FLAG_INDICATION, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_QualifierDecl Units_qual_decl =
{
    MI_T("Units"), /* name */
    MI_STRING, /* type */
    MI_FLAG_METHOD|MI_FLAG_PARAMETER|MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_QualifierDecl ValueMap_qual_decl =
{
    MI_T("ValueMap"), /* name */
    MI_STRINGA, /* type */
    MI_FLAG_METHOD|MI_FLAG_PARAMETER|MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_QualifierDecl Values_qual_decl =
{
    MI_T("Values"), /* name */
    MI_STRINGA, /* type */
    MI_FLAG_METHOD|MI_FLAG_PARAMETER|MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_QualifierDecl Version_qual_decl =
{
    MI_T("Version"), /* name */
    MI_STRING, /* type */
    MI_FLAG_ASSOCIATION|MI_FLAG_CLASS|MI_FLAG_INDICATION, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TRANSLATABLE|MI_FLAG_RESTRICTED, /* flavor */
    0, /* subscript */
    NULL, /* value */
};

static MI_CONST MI_Boolean Weak_qual_decl_value = 0;

static MI_CONST MI_QualifierDecl Weak_qual_decl =
{
    MI_T("Weak"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_REFERENCE, /* scope */
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &Weak_qual_decl_value, /* value */
};

static MI_CONST MI_Boolean Write_qual_decl_value = 0;

static MI_CONST MI_QualifierDecl Write_qual_decl =
{
    MI_T("Write"), /* name */
    MI_BOOLEAN, /* type */
    MI_FLAG_PROPERTY, /* scope */
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS, /* flavor */
    0, /* subscript */
    &Write_qual_decl_value, /* value */
};

static MI_QualifierDecl MI_CONST* MI_CONST qualifierDecls[] =
{
    &Abstract_qual_decl,
    &Aggregate_qual_decl,
    &Aggregation_qual_decl,
    &ArrayType_qual_decl,
    &Association_qual_decl,
    &BitMap_qual_decl,
    &BitValues_qual_decl,
    &ClassConstraint_qual_decl,
    &ClassVersion_qual_decl,
    &Composition_qual_decl,
    &Correlatable_qual_decl,
    &Counter_qual_decl,
    &Deprecated_qual_decl,
    &Description_qual_decl,
    &DisplayName_qual_decl,
    &DN_qual_decl,
    &EmbeddedInstance_qual_decl,
    &EmbeddedObject_qual_decl,
    &Exception_qual_decl,
    &Experimental_qual_decl,
    &Gauge_qual_decl,
    &In_qual_decl,
    &Indication_qual_decl,
    &IsPUnit_qual_decl,
    &Key_qual_decl,
    &MappingStrings_qual_decl,
    &Max_qual_decl,
    &MaxLen_qual_decl,
    &MaxValue_qual_decl,
    &MethodConstraint_qual_decl,
    &Min_qual_decl,
    &MinLen_qual_decl,
    &MinValue_qual_decl,
    &ModelCorrespondence_qual_decl,
    &Nonlocal_qual_decl,
    &NonlocalType_qual_decl,
    &NullValue_qual_decl,
    &Octetstring_qual_decl,
    &Out_qual_decl,
    &Override_qual_decl,
    &Propagated_qual_decl,
    &PropertyConstraint_qual_decl,
    &PUnit_qual_decl,
    &Read_qual_decl,
    &Required_qual_decl,
    &Revision_qual_decl,
    &Schema_qual_decl,
    &Source_qual_decl,
    &SourceType_qual_decl,
    &Static_qual_decl,
    &Stream_qual_decl,
    &Terminal_qual_decl,
    &UMLPackagePath_qual_decl,
    &Units_qual_decl,
    &ValueMap_qual_decl,
    &Values_qual_decl,
    &Version_qual_decl,
    &Weak_qual_decl,
    &Write_qual_decl,
};

/*
**==============================================================================
**
** OMI_BaseResource
**
**==============================================================================
*/


static MI_CONST MI_Boolean OMI_BaseResource_Abstract_qual_value = 1;

static MI_CONST MI_Qualifier OMI_BaseResource_Abstract_qual =
{
    MI_T("Abstract"),
    MI_BOOLEAN,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_RESTRICTED,
    &OMI_BaseResource_Abstract_qual_value
};

static MI_CONST MI_Char* OMI_BaseResource_ClassVersion_qual_value = MI_T("1.0.0");

static MI_CONST MI_Qualifier OMI_BaseResource_ClassVersion_qual =
{
    MI_T("ClassVersion"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_RESTRICTED,
    &OMI_BaseResource_ClassVersion_qual_value
};

static MI_CONST MI_Char* OMI_BaseResource_Description_qual_value = MI_T("1");

static MI_CONST MI_Qualifier OMI_BaseResource_Description_qual =
{
    MI_T("Description"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE,
    &OMI_BaseResource_Description_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST OMI_BaseResource_quals[] =
{
    &OMI_BaseResource_Abstract_qual,
    &OMI_BaseResource_ClassVersion_qual,
    &OMI_BaseResource_Description_qual,
};

/* class OMI_BaseResource */
MI_CONST MI_ClassDecl OMI_BaseResource_rtti =
{
    MI_FLAG_CLASS|MI_FLAG_ABSTRACT, /* flags */
    0x006F6510, /* code */
    MI_T("OMI_BaseResource"), /* name */
    OMI_BaseResource_quals, /* qualifiers */
    MI_COUNT(OMI_BaseResource_quals), /* numQualifiers */
    NULL, /* properties */
    0, /* numProperties */
    sizeof(OMI_BaseResource), /* size */
    NULL, /* superClass */
    NULL, /* superClassDecl */
    NULL, /* methods */
    0, /* numMethods */
    &schemaDecl, /* schema */
    NULL, /* functions */
    NULL /* owningClass */
};

/*
**==============================================================================
**
** MSFT_nxOMSPerfCounterObject
**
**==============================================================================
*/

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterObject_ObjectName_Key_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterObject_ObjectName_Key_qual =
{
    MI_T("Key"),
    MI_BOOLEAN,
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterObject_ObjectName_Key_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterObject_ObjectName_quals[] =
{
    &MSFT_nxOMSPerfCounterObject_ObjectName_Key_qual,
};

/* property MSFT_nxOMSPerfCounterObject.ObjectName */
static MI_CONST MI_PropertyDecl MSFT_nxOMSPerfCounterObject_ObjectName_prop =
{
    MI_FLAG_PROPERTY|MI_FLAG_KEY|MI_FLAG_READONLY, /* flags */
    0x006F650A, /* code */
    MI_T("ObjectName"), /* name */
    MSFT_nxOMSPerfCounterObject_ObjectName_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterObject_ObjectName_quals), /* numQualifiers */
    MI_STRING, /* type */
    NULL, /* className */
    0, /* subscript */
    offsetof(MSFT_nxOMSPerfCounterObject, ObjectName), /* offset */
    MI_T("MSFT_nxOMSPerfCounterObject"), /* origin */
    MI_T("MSFT_nxOMSPerfCounterObject"), /* propagator */
    NULL,
};

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterObject_InstanceName_Write_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterObject_InstanceName_Write_qual =
{
    MI_T("Write"),
    MI_BOOLEAN,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterObject_InstanceName_Write_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterObject_InstanceName_quals[] =
{
    &MSFT_nxOMSPerfCounterObject_InstanceName_Write_qual,
};

/* property MSFT_nxOMSPerfCounterObject.InstanceName */
static MI_CONST MI_PropertyDecl MSFT_nxOMSPerfCounterObject_InstanceName_prop =
{
    MI_FLAG_PROPERTY, /* flags */
    0x0069650C, /* code */
    MI_T("InstanceName"), /* name */
    MSFT_nxOMSPerfCounterObject_InstanceName_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterObject_InstanceName_quals), /* numQualifiers */
    MI_STRING, /* type */
    NULL, /* className */
    0, /* subscript */
    offsetof(MSFT_nxOMSPerfCounterObject, InstanceName), /* offset */
    MI_T("MSFT_nxOMSPerfCounterObject"), /* origin */
    MI_T("MSFT_nxOMSPerfCounterObject"), /* propagator */
    NULL,
};

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterObject_AllInstances_Write_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterObject_AllInstances_Write_qual =
{
    MI_T("Write"),
    MI_BOOLEAN,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterObject_AllInstances_Write_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterObject_AllInstances_quals[] =
{
    &MSFT_nxOMSPerfCounterObject_AllInstances_Write_qual,
};

/* property MSFT_nxOMSPerfCounterObject.AllInstances */
static MI_CONST MI_PropertyDecl MSFT_nxOMSPerfCounterObject_AllInstances_prop =
{
    MI_FLAG_PROPERTY, /* flags */
    0x0061730C, /* code */
    MI_T("AllInstances"), /* name */
    MSFT_nxOMSPerfCounterObject_AllInstances_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterObject_AllInstances_quals), /* numQualifiers */
    MI_BOOLEAN, /* type */
    NULL, /* className */
    0, /* subscript */
    offsetof(MSFT_nxOMSPerfCounterObject, AllInstances), /* offset */
    MI_T("MSFT_nxOMSPerfCounterObject"), /* origin */
    MI_T("MSFT_nxOMSPerfCounterObject"), /* propagator */
    NULL,
};

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterObject_IntervalSeconds_Write_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterObject_IntervalSeconds_Write_qual =
{
    MI_T("Write"),
    MI_BOOLEAN,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterObject_IntervalSeconds_Write_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterObject_IntervalSeconds_quals[] =
{
    &MSFT_nxOMSPerfCounterObject_IntervalSeconds_Write_qual,
};

/* property MSFT_nxOMSPerfCounterObject.IntervalSeconds */
static MI_CONST MI_PropertyDecl MSFT_nxOMSPerfCounterObject_IntervalSeconds_prop =
{
    MI_FLAG_PROPERTY, /* flags */
    0x0069730F, /* code */
    MI_T("IntervalSeconds"), /* name */
    MSFT_nxOMSPerfCounterObject_IntervalSeconds_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterObject_IntervalSeconds_quals), /* numQualifiers */
    MI_UINT16, /* type */
    NULL, /* className */
    0, /* subscript */
    offsetof(MSFT_nxOMSPerfCounterObject, IntervalSeconds), /* offset */
    MI_T("MSFT_nxOMSPerfCounterObject"), /* origin */
    MI_T("MSFT_nxOMSPerfCounterObject"), /* propagator */
    NULL,
};

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterObject_PerformanceCounter_Write_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterObject_PerformanceCounter_Write_qual =
{
    MI_T("Write"),
    MI_BOOLEAN,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterObject_PerformanceCounter_Write_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterObject_PerformanceCounter_quals[] =
{
    &MSFT_nxOMSPerfCounterObject_PerformanceCounter_Write_qual,
};

/* property MSFT_nxOMSPerfCounterObject.PerformanceCounter */
static MI_CONST MI_PropertyDecl MSFT_nxOMSPerfCounterObject_PerformanceCounter_prop =
{
    MI_FLAG_PROPERTY, /* flags */
    0x00707212, /* code */
    MI_T("PerformanceCounter"), /* name */
    MSFT_nxOMSPerfCounterObject_PerformanceCounter_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterObject_PerformanceCounter_quals), /* numQualifiers */
    MI_STRINGA, /* type */
    NULL, /* className */
    0, /* subscript */
    offsetof(MSFT_nxOMSPerfCounterObject, PerformanceCounter), /* offset */
    MI_T("MSFT_nxOMSPerfCounterObject"), /* origin */
    MI_T("MSFT_nxOMSPerfCounterObject"), /* propagator */
    NULL,
};

static MI_PropertyDecl MI_CONST* MI_CONST MSFT_nxOMSPerfCounterObject_props[] =
{
    &MSFT_nxOMSPerfCounterObject_ObjectName_prop,
    &MSFT_nxOMSPerfCounterObject_InstanceName_prop,
    &MSFT_nxOMSPerfCounterObject_AllInstances_prop,
    &MSFT_nxOMSPerfCounterObject_IntervalSeconds_prop,
    &MSFT_nxOMSPerfCounterObject_PerformanceCounter_prop,
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterObject_ClassVersion_qual_value = MI_T("1.0.0");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterObject_ClassVersion_qual =
{
    MI_T("ClassVersion"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_RESTRICTED,
    &MSFT_nxOMSPerfCounterObject_ClassVersion_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterObject_quals[] =
{
    &MSFT_nxOMSPerfCounterObject_ClassVersion_qual,
};

/* class MSFT_nxOMSPerfCounterObject */
MI_CONST MI_ClassDecl MSFT_nxOMSPerfCounterObject_rtti =
{
    MI_FLAG_CLASS, /* flags */
    0x006D741B, /* code */
    MI_T("MSFT_nxOMSPerfCounterObject"), /* name */
    MSFT_nxOMSPerfCounterObject_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterObject_quals), /* numQualifiers */
    MSFT_nxOMSPerfCounterObject_props, /* properties */
    MI_COUNT(MSFT_nxOMSPerfCounterObject_props), /* numProperties */
    sizeof(MSFT_nxOMSPerfCounterObject), /* size */
    NULL, /* superClass */
    NULL, /* superClassDecl */
    NULL, /* methods */
    0, /* numMethods */
    &schemaDecl, /* schema */
    NULL, /* functions */
    NULL /* owningClass */
};

/*
**==============================================================================
**
** MSFT_nxOMSPerfCounterResource
**
**==============================================================================
*/

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterResource_Name_Key_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_Name_Key_qual =
{
    MI_T("Key"),
    MI_BOOLEAN,
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_Name_Key_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_Name_quals[] =
{
    &MSFT_nxOMSPerfCounterResource_Name_Key_qual,
};

/* property MSFT_nxOMSPerfCounterResource.Name */
static MI_CONST MI_PropertyDecl MSFT_nxOMSPerfCounterResource_Name_prop =
{
    MI_FLAG_PROPERTY|MI_FLAG_KEY|MI_FLAG_READONLY, /* flags */
    0x006E6504, /* code */
    MI_T("Name"), /* name */
    MSFT_nxOMSPerfCounterResource_Name_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_Name_quals), /* numQualifiers */
    MI_STRING, /* type */
    NULL, /* className */
    0, /* subscript */
    offsetof(MSFT_nxOMSPerfCounterResource, Name), /* offset */
    MI_T("MSFT_nxOMSPerfCounterResource"), /* origin */
    MI_T("MSFT_nxOMSPerfCounterResource"), /* propagator */
    NULL,
};

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterResource_WorkspaceID_Key_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_WorkspaceID_Key_qual =
{
    MI_T("Key"),
    MI_BOOLEAN,
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_WorkspaceID_Key_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_WorkspaceID_quals[] =
{
    &MSFT_nxOMSPerfCounterResource_WorkspaceID_Key_qual,
};

/* property MSFT_nxOMSPerfCounterResource.WorkspaceID */
static MI_CONST MI_PropertyDecl MSFT_nxOMSPerfCounterResource_WorkspaceID_prop =
{
    MI_FLAG_PROPERTY|MI_FLAG_KEY|MI_FLAG_READONLY, /* flags */
    0x0077640B, /* code */
    MI_T("WorkspaceID"), /* name */
    MSFT_nxOMSPerfCounterResource_WorkspaceID_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_WorkspaceID_quals), /* numQualifiers */
    MI_STRING, /* type */
    NULL, /* className */
    0, /* subscript */
    offsetof(MSFT_nxOMSPerfCounterResource, WorkspaceID), /* offset */
    MI_T("MSFT_nxOMSPerfCounterResource"), /* origin */
    MI_T("MSFT_nxOMSPerfCounterResource"), /* propagator */
    NULL,
};

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterResource_HeartbeatIntervalSeconds_Write_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_HeartbeatIntervalSeconds_Write_qual =
{
    MI_T("Write"),
    MI_BOOLEAN,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_HeartbeatIntervalSeconds_Write_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_HeartbeatIntervalSeconds_quals[] =
{
    &MSFT_nxOMSPerfCounterResource_HeartbeatIntervalSeconds_Write_qual,
};

/* property MSFT_nxOMSPerfCounterResource.HeartbeatIntervalSeconds */
static MI_CONST MI_PropertyDecl MSFT_nxOMSPerfCounterResource_HeartbeatIntervalSeconds_prop =
{
    MI_FLAG_PROPERTY, /* flags */
    0x00687318, /* code */
    MI_T("HeartbeatIntervalSeconds"), /* name */
    MSFT_nxOMSPerfCounterResource_HeartbeatIntervalSeconds_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_HeartbeatIntervalSeconds_quals), /* numQualifiers */
    MI_UINT16, /* type */
    NULL, /* className */
    0, /* subscript */
    offsetof(MSFT_nxOMSPerfCounterResource, HeartbeatIntervalSeconds), /* offset */
    MI_T("MSFT_nxOMSPerfCounterResource"), /* origin */
    MI_T("MSFT_nxOMSPerfCounterResource"), /* propagator */
    NULL,
};

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterResource_PerfCounterObject_Write_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_PerfCounterObject_Write_qual =
{
    MI_T("Write"),
    MI_BOOLEAN,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_PerfCounterObject_Write_qual_value
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterResource_PerfCounterObject_EmbeddedInstance_qual_value = MI_T("MSFT_nxOMSPerfCounterObject");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_PerfCounterObject_EmbeddedInstance_qual =
{
    MI_T("EmbeddedInstance"),
    MI_STRING,
    MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_PerfCounterObject_EmbeddedInstance_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_PerfCounterObject_quals[] =
{
    &MSFT_nxOMSPerfCounterResource_PerfCounterObject_Write_qual,
    &MSFT_nxOMSPerfCounterResource_PerfCounterObject_EmbeddedInstance_qual,
};

/* property MSFT_nxOMSPerfCounterResource.PerfCounterObject */
static MI_CONST MI_PropertyDecl MSFT_nxOMSPerfCounterResource_PerfCounterObject_prop =
{
    MI_FLAG_PROPERTY, /* flags */
    0x00707411, /* code */
    MI_T("PerfCounterObject"), /* name */
    MSFT_nxOMSPerfCounterResource_PerfCounterObject_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_PerfCounterObject_quals), /* numQualifiers */
    MI_INSTANCEA, /* type */
    MI_T("MSFT_nxOMSPerfCounterObject"), /* className */
    0, /* subscript */
    offsetof(MSFT_nxOMSPerfCounterResource, PerfCounterObject), /* offset */
    MI_T("MSFT_nxOMSPerfCounterResource"), /* origin */
    MI_T("MSFT_nxOMSPerfCounterResource"), /* propagator */
    NULL,
};

static MI_PropertyDecl MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_props[] =
{
    &MSFT_nxOMSPerfCounterResource_Name_prop,
    &MSFT_nxOMSPerfCounterResource_WorkspaceID_prop,
    &MSFT_nxOMSPerfCounterResource_HeartbeatIntervalSeconds_prop,
    &MSFT_nxOMSPerfCounterResource_PerfCounterObject_prop,
};

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterResource_GetTargetResource_Static_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_GetTargetResource_Static_qual =
{
    MI_T("Static"),
    MI_BOOLEAN,
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_Static_qual_value
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterResource_GetTargetResource_Description_qual_value = MI_T("2");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_GetTargetResource_Description_qual =
{
    MI_T("Description"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE,
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_Description_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_GetTargetResource_quals[] =
{
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_Static_qual,
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_Description_qual,
};

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterResource_GetTargetResource_InputResource_In_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_GetTargetResource_InputResource_In_qual =
{
    MI_T("In"),
    MI_BOOLEAN,
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_InputResource_In_qual_value
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterResource_GetTargetResource_InputResource_EmbeddedInstance_qual_value = MI_T("MSFT_nxOMSPerfCounterResource");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_GetTargetResource_InputResource_EmbeddedInstance_qual =
{
    MI_T("EmbeddedInstance"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_InputResource_EmbeddedInstance_qual_value
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterResource_GetTargetResource_InputResource_Description_qual_value = MI_T("3");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_GetTargetResource_InputResource_Description_qual =
{
    MI_T("Description"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE,
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_InputResource_Description_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_GetTargetResource_InputResource_quals[] =
{
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_InputResource_In_qual,
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_InputResource_EmbeddedInstance_qual,
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_InputResource_Description_qual,
};

/* parameter MSFT_nxOMSPerfCounterResource.GetTargetResource(): InputResource */
static MI_CONST MI_ParameterDecl MSFT_nxOMSPerfCounterResource_GetTargetResource_InputResource_param =
{
    MI_FLAG_PARAMETER|MI_FLAG_IN, /* flags */
    0x0069650D, /* code */
    MI_T("InputResource"), /* name */
    MSFT_nxOMSPerfCounterResource_GetTargetResource_InputResource_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_GetTargetResource_InputResource_quals), /* numQualifiers */
    MI_INSTANCE, /* type */
    MI_T("MSFT_nxOMSPerfCounterResource"), /* className */
    0, /* subscript */
    offsetof(MSFT_nxOMSPerfCounterResource_GetTargetResource, InputResource), /* offset */
};

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterResource_GetTargetResource_Flags_In_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_GetTargetResource_Flags_In_qual =
{
    MI_T("In"),
    MI_BOOLEAN,
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_Flags_In_qual_value
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterResource_GetTargetResource_Flags_Description_qual_value = MI_T("4");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_GetTargetResource_Flags_Description_qual =
{
    MI_T("Description"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE,
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_Flags_Description_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_GetTargetResource_Flags_quals[] =
{
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_Flags_In_qual,
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_Flags_Description_qual,
};

/* parameter MSFT_nxOMSPerfCounterResource.GetTargetResource(): Flags */
static MI_CONST MI_ParameterDecl MSFT_nxOMSPerfCounterResource_GetTargetResource_Flags_param =
{
    MI_FLAG_PARAMETER|MI_FLAG_IN, /* flags */
    0x00667305, /* code */
    MI_T("Flags"), /* name */
    MSFT_nxOMSPerfCounterResource_GetTargetResource_Flags_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_GetTargetResource_Flags_quals), /* numQualifiers */
    MI_UINT32, /* type */
    NULL, /* className */
    0, /* subscript */
    offsetof(MSFT_nxOMSPerfCounterResource_GetTargetResource, Flags), /* offset */
};

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterResource_GetTargetResource_OutputResource_Out_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_GetTargetResource_OutputResource_Out_qual =
{
    MI_T("Out"),
    MI_BOOLEAN,
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_OutputResource_Out_qual_value
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterResource_GetTargetResource_OutputResource_EmbeddedInstance_qual_value = MI_T("MSFT_nxOMSPerfCounterResource");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_GetTargetResource_OutputResource_EmbeddedInstance_qual =
{
    MI_T("EmbeddedInstance"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_OutputResource_EmbeddedInstance_qual_value
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterResource_GetTargetResource_OutputResource_Description_qual_value = MI_T("5");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_GetTargetResource_OutputResource_Description_qual =
{
    MI_T("Description"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE,
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_OutputResource_Description_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_GetTargetResource_OutputResource_quals[] =
{
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_OutputResource_Out_qual,
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_OutputResource_EmbeddedInstance_qual,
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_OutputResource_Description_qual,
};

/* parameter MSFT_nxOMSPerfCounterResource.GetTargetResource(): OutputResource */
static MI_CONST MI_ParameterDecl MSFT_nxOMSPerfCounterResource_GetTargetResource_OutputResource_param =
{
    MI_FLAG_PARAMETER|MI_FLAG_OUT, /* flags */
    0x006F650E, /* code */
    MI_T("OutputResource"), /* name */
    MSFT_nxOMSPerfCounterResource_GetTargetResource_OutputResource_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_GetTargetResource_OutputResource_quals), /* numQualifiers */
    MI_INSTANCE, /* type */
    MI_T("MSFT_nxOMSPerfCounterResource"), /* className */
    0, /* subscript */
    offsetof(MSFT_nxOMSPerfCounterResource_GetTargetResource, OutputResource), /* offset */
};

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterResource_GetTargetResource_MIReturn_Static_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_GetTargetResource_MIReturn_Static_qual =
{
    MI_T("Static"),
    MI_BOOLEAN,
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_MIReturn_Static_qual_value
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterResource_GetTargetResource_MIReturn_Description_qual_value = MI_T("2");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_GetTargetResource_MIReturn_Description_qual =
{
    MI_T("Description"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE,
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_MIReturn_Description_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_GetTargetResource_MIReturn_quals[] =
{
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_MIReturn_Static_qual,
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_MIReturn_Description_qual,
};

/* parameter MSFT_nxOMSPerfCounterResource.GetTargetResource(): MIReturn */
static MI_CONST MI_ParameterDecl MSFT_nxOMSPerfCounterResource_GetTargetResource_MIReturn_param =
{
    MI_FLAG_PARAMETER|MI_FLAG_OUT, /* flags */
    0x006D6E08, /* code */
    MI_T("MIReturn"), /* name */
    MSFT_nxOMSPerfCounterResource_GetTargetResource_MIReturn_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_GetTargetResource_MIReturn_quals), /* numQualifiers */
    MI_UINT32, /* type */
    NULL, /* className */
    0, /* subscript */
    offsetof(MSFT_nxOMSPerfCounterResource_GetTargetResource, MIReturn), /* offset */
};

static MI_ParameterDecl MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_GetTargetResource_params[] =
{
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_MIReturn_param,
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_InputResource_param,
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_Flags_param,
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_OutputResource_param,
};

/* method MSFT_nxOMSPerfCounterResource.GetTargetResource() */
MI_CONST MI_MethodDecl MSFT_nxOMSPerfCounterResource_GetTargetResource_rtti =
{
    MI_FLAG_METHOD|MI_FLAG_STATIC, /* flags */
    0x00676511, /* code */
    MI_T("GetTargetResource"), /* name */
    MSFT_nxOMSPerfCounterResource_GetTargetResource_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_GetTargetResource_quals), /* numQualifiers */
    MSFT_nxOMSPerfCounterResource_GetTargetResource_params, /* parameters */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_GetTargetResource_params), /* numParameters */
    sizeof(MSFT_nxOMSPerfCounterResource_GetTargetResource), /* size */
    MI_UINT32, /* returnType */
    MI_T("MSFT_nxOMSPerfCounterResource"), /* origin */
    MI_T("MSFT_nxOMSPerfCounterResource"), /* propagator */
    &schemaDecl, /* schema */
    (MI_ProviderFT_Invoke)MSFT_nxOMSPerfCounterResource_Invoke_GetTargetResource, /* method */
};

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterResource_TestTargetResource_Static_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_TestTargetResource_Static_qual =
{
    MI_T("Static"),
    MI_BOOLEAN,
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_Static_qual_value
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterResource_TestTargetResource_Description_qual_value = MI_T("6");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_TestTargetResource_Description_qual =
{
    MI_T("Description"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_Description_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_TestTargetResource_quals[] =
{
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_Static_qual,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_Description_qual,
};

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterResource_TestTargetResource_InputResource_In_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_TestTargetResource_InputResource_In_qual =
{
    MI_T("In"),
    MI_BOOLEAN,
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_InputResource_In_qual_value
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterResource_TestTargetResource_InputResource_EmbeddedInstance_qual_value = MI_T("MSFT_nxOMSPerfCounterResource");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_TestTargetResource_InputResource_EmbeddedInstance_qual =
{
    MI_T("EmbeddedInstance"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_InputResource_EmbeddedInstance_qual_value
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterResource_TestTargetResource_InputResource_Description_qual_value = MI_T("7");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_TestTargetResource_InputResource_Description_qual =
{
    MI_T("Description"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_InputResource_Description_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_TestTargetResource_InputResource_quals[] =
{
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_InputResource_In_qual,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_InputResource_EmbeddedInstance_qual,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_InputResource_Description_qual,
};

/* parameter MSFT_nxOMSPerfCounterResource.TestTargetResource(): InputResource */
static MI_CONST MI_ParameterDecl MSFT_nxOMSPerfCounterResource_TestTargetResource_InputResource_param =
{
    MI_FLAG_PARAMETER|MI_FLAG_IN, /* flags */
    0x0069650D, /* code */
    MI_T("InputResource"), /* name */
    MSFT_nxOMSPerfCounterResource_TestTargetResource_InputResource_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_TestTargetResource_InputResource_quals), /* numQualifiers */
    MI_INSTANCE, /* type */
    MI_T("MSFT_nxOMSPerfCounterResource"), /* className */
    0, /* subscript */
    offsetof(MSFT_nxOMSPerfCounterResource_TestTargetResource, InputResource), /* offset */
};

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterResource_TestTargetResource_Flags_In_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_TestTargetResource_Flags_In_qual =
{
    MI_T("In"),
    MI_BOOLEAN,
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_Flags_In_qual_value
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterResource_TestTargetResource_Flags_Description_qual_value = MI_T("8");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_TestTargetResource_Flags_Description_qual =
{
    MI_T("Description"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_Flags_Description_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_TestTargetResource_Flags_quals[] =
{
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_Flags_In_qual,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_Flags_Description_qual,
};

/* parameter MSFT_nxOMSPerfCounterResource.TestTargetResource(): Flags */
static MI_CONST MI_ParameterDecl MSFT_nxOMSPerfCounterResource_TestTargetResource_Flags_param =
{
    MI_FLAG_PARAMETER|MI_FLAG_IN, /* flags */
    0x00667305, /* code */
    MI_T("Flags"), /* name */
    MSFT_nxOMSPerfCounterResource_TestTargetResource_Flags_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_TestTargetResource_Flags_quals), /* numQualifiers */
    MI_UINT32, /* type */
    NULL, /* className */
    0, /* subscript */
    offsetof(MSFT_nxOMSPerfCounterResource_TestTargetResource, Flags), /* offset */
};

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterResource_TestTargetResource_Result_Out_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_TestTargetResource_Result_Out_qual =
{
    MI_T("Out"),
    MI_BOOLEAN,
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_Result_Out_qual_value
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterResource_TestTargetResource_Result_Description_qual_value = MI_T("9");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_TestTargetResource_Result_Description_qual =
{
    MI_T("Description"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_Result_Description_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_TestTargetResource_Result_quals[] =
{
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_Result_Out_qual,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_Result_Description_qual,
};

/* parameter MSFT_nxOMSPerfCounterResource.TestTargetResource(): Result */
static MI_CONST MI_ParameterDecl MSFT_nxOMSPerfCounterResource_TestTargetResource_Result_param =
{
    MI_FLAG_PARAMETER|MI_FLAG_OUT, /* flags */
    0x00727406, /* code */
    MI_T("Result"), /* name */
    MSFT_nxOMSPerfCounterResource_TestTargetResource_Result_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_TestTargetResource_Result_quals), /* numQualifiers */
    MI_BOOLEAN, /* type */
    NULL, /* className */
    0, /* subscript */
    offsetof(MSFT_nxOMSPerfCounterResource_TestTargetResource, Result), /* offset */
};

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterResource_TestTargetResource_ProviderContext_Out_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_TestTargetResource_ProviderContext_Out_qual =
{
    MI_T("Out"),
    MI_BOOLEAN,
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_ProviderContext_Out_qual_value
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterResource_TestTargetResource_ProviderContext_Description_qual_value = MI_T("10");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_TestTargetResource_ProviderContext_Description_qual =
{
    MI_T("Description"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_ProviderContext_Description_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_TestTargetResource_ProviderContext_quals[] =
{
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_ProviderContext_Out_qual,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_ProviderContext_Description_qual,
};

/* parameter MSFT_nxOMSPerfCounterResource.TestTargetResource(): ProviderContext */
static MI_CONST MI_ParameterDecl MSFT_nxOMSPerfCounterResource_TestTargetResource_ProviderContext_param =
{
    MI_FLAG_PARAMETER|MI_FLAG_OUT, /* flags */
    0x0070740F, /* code */
    MI_T("ProviderContext"), /* name */
    MSFT_nxOMSPerfCounterResource_TestTargetResource_ProviderContext_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_TestTargetResource_ProviderContext_quals), /* numQualifiers */
    MI_UINT64, /* type */
    NULL, /* className */
    0, /* subscript */
    offsetof(MSFT_nxOMSPerfCounterResource_TestTargetResource, ProviderContext), /* offset */
};

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterResource_TestTargetResource_MIReturn_Static_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_TestTargetResource_MIReturn_Static_qual =
{
    MI_T("Static"),
    MI_BOOLEAN,
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_MIReturn_Static_qual_value
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterResource_TestTargetResource_MIReturn_Description_qual_value = MI_T("6");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_TestTargetResource_MIReturn_Description_qual =
{
    MI_T("Description"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_MIReturn_Description_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_TestTargetResource_MIReturn_quals[] =
{
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_MIReturn_Static_qual,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_MIReturn_Description_qual,
};

/* parameter MSFT_nxOMSPerfCounterResource.TestTargetResource(): MIReturn */
static MI_CONST MI_ParameterDecl MSFT_nxOMSPerfCounterResource_TestTargetResource_MIReturn_param =
{
    MI_FLAG_PARAMETER|MI_FLAG_OUT, /* flags */
    0x006D6E08, /* code */
    MI_T("MIReturn"), /* name */
    MSFT_nxOMSPerfCounterResource_TestTargetResource_MIReturn_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_TestTargetResource_MIReturn_quals), /* numQualifiers */
    MI_UINT32, /* type */
    NULL, /* className */
    0, /* subscript */
    offsetof(MSFT_nxOMSPerfCounterResource_TestTargetResource, MIReturn), /* offset */
};

static MI_ParameterDecl MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_TestTargetResource_params[] =
{
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_MIReturn_param,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_InputResource_param,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_Flags_param,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_Result_param,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_ProviderContext_param,
};

/* method MSFT_nxOMSPerfCounterResource.TestTargetResource() */
MI_CONST MI_MethodDecl MSFT_nxOMSPerfCounterResource_TestTargetResource_rtti =
{
    MI_FLAG_METHOD|MI_FLAG_STATIC, /* flags */
    0x00746512, /* code */
    MI_T("TestTargetResource"), /* name */
    MSFT_nxOMSPerfCounterResource_TestTargetResource_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_TestTargetResource_quals), /* numQualifiers */
    MSFT_nxOMSPerfCounterResource_TestTargetResource_params, /* parameters */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_TestTargetResource_params), /* numParameters */
    sizeof(MSFT_nxOMSPerfCounterResource_TestTargetResource), /* size */
    MI_UINT32, /* returnType */
    MI_T("MSFT_nxOMSPerfCounterResource"), /* origin */
    MI_T("MSFT_nxOMSPerfCounterResource"), /* propagator */
    &schemaDecl, /* schema */
    (MI_ProviderFT_Invoke)MSFT_nxOMSPerfCounterResource_Invoke_TestTargetResource, /* method */
};

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterResource_SetTargetResource_Static_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_SetTargetResource_Static_qual =
{
    MI_T("Static"),
    MI_BOOLEAN,
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_Static_qual_value
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterResource_SetTargetResource_Description_qual_value = MI_T("11");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_SetTargetResource_Description_qual =
{
    MI_T("Description"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE,
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_Description_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_SetTargetResource_quals[] =
{
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_Static_qual,
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_Description_qual,
};

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterResource_SetTargetResource_InputResource_In_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_SetTargetResource_InputResource_In_qual =
{
    MI_T("In"),
    MI_BOOLEAN,
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_InputResource_In_qual_value
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterResource_SetTargetResource_InputResource_EmbeddedInstance_qual_value = MI_T("MSFT_nxOMSPerfCounterResource");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_SetTargetResource_InputResource_EmbeddedInstance_qual =
{
    MI_T("EmbeddedInstance"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_InputResource_EmbeddedInstance_qual_value
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterResource_SetTargetResource_InputResource_Description_qual_value = MI_T("7");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_SetTargetResource_InputResource_Description_qual =
{
    MI_T("Description"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE,
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_InputResource_Description_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_SetTargetResource_InputResource_quals[] =
{
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_InputResource_In_qual,
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_InputResource_EmbeddedInstance_qual,
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_InputResource_Description_qual,
};

/* parameter MSFT_nxOMSPerfCounterResource.SetTargetResource(): InputResource */
static MI_CONST MI_ParameterDecl MSFT_nxOMSPerfCounterResource_SetTargetResource_InputResource_param =
{
    MI_FLAG_PARAMETER|MI_FLAG_IN, /* flags */
    0x0069650D, /* code */
    MI_T("InputResource"), /* name */
    MSFT_nxOMSPerfCounterResource_SetTargetResource_InputResource_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_SetTargetResource_InputResource_quals), /* numQualifiers */
    MI_INSTANCE, /* type */
    MI_T("MSFT_nxOMSPerfCounterResource"), /* className */
    0, /* subscript */
    offsetof(MSFT_nxOMSPerfCounterResource_SetTargetResource, InputResource), /* offset */
};

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterResource_SetTargetResource_ProviderContext_In_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_SetTargetResource_ProviderContext_In_qual =
{
    MI_T("In"),
    MI_BOOLEAN,
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_ProviderContext_In_qual_value
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterResource_SetTargetResource_ProviderContext_Description_qual_value = MI_T("12");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_SetTargetResource_ProviderContext_Description_qual =
{
    MI_T("Description"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE,
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_ProviderContext_Description_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_SetTargetResource_ProviderContext_quals[] =
{
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_ProviderContext_In_qual,
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_ProviderContext_Description_qual,
};

/* parameter MSFT_nxOMSPerfCounterResource.SetTargetResource(): ProviderContext */
static MI_CONST MI_ParameterDecl MSFT_nxOMSPerfCounterResource_SetTargetResource_ProviderContext_param =
{
    MI_FLAG_PARAMETER|MI_FLAG_IN, /* flags */
    0x0070740F, /* code */
    MI_T("ProviderContext"), /* name */
    MSFT_nxOMSPerfCounterResource_SetTargetResource_ProviderContext_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_SetTargetResource_ProviderContext_quals), /* numQualifiers */
    MI_UINT64, /* type */
    NULL, /* className */
    0, /* subscript */
    offsetof(MSFT_nxOMSPerfCounterResource_SetTargetResource, ProviderContext), /* offset */
};

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterResource_SetTargetResource_Flags_In_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_SetTargetResource_Flags_In_qual =
{
    MI_T("In"),
    MI_BOOLEAN,
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_Flags_In_qual_value
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterResource_SetTargetResource_Flags_Description_qual_value = MI_T("8");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_SetTargetResource_Flags_Description_qual =
{
    MI_T("Description"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE,
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_Flags_Description_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_SetTargetResource_Flags_quals[] =
{
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_Flags_In_qual,
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_Flags_Description_qual,
};

/* parameter MSFT_nxOMSPerfCounterResource.SetTargetResource(): Flags */
static MI_CONST MI_ParameterDecl MSFT_nxOMSPerfCounterResource_SetTargetResource_Flags_param =
{
    MI_FLAG_PARAMETER|MI_FLAG_IN, /* flags */
    0x00667305, /* code */
    MI_T("Flags"), /* name */
    MSFT_nxOMSPerfCounterResource_SetTargetResource_Flags_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_SetTargetResource_Flags_quals), /* numQualifiers */
    MI_UINT32, /* type */
    NULL, /* className */
    0, /* subscript */
    offsetof(MSFT_nxOMSPerfCounterResource_SetTargetResource, Flags), /* offset */
};

static MI_CONST MI_Boolean MSFT_nxOMSPerfCounterResource_SetTargetResource_MIReturn_Static_qual_value = 1;

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_SetTargetResource_MIReturn_Static_qual =
{
    MI_T("Static"),
    MI_BOOLEAN,
    MI_FLAG_DISABLEOVERRIDE|MI_FLAG_TOSUBCLASS,
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_MIReturn_Static_qual_value
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterResource_SetTargetResource_MIReturn_Description_qual_value = MI_T("11");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_SetTargetResource_MIReturn_Description_qual =
{
    MI_T("Description"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE,
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_MIReturn_Description_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_SetTargetResource_MIReturn_quals[] =
{
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_MIReturn_Static_qual,
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_MIReturn_Description_qual,
};

/* parameter MSFT_nxOMSPerfCounterResource.SetTargetResource(): MIReturn */
static MI_CONST MI_ParameterDecl MSFT_nxOMSPerfCounterResource_SetTargetResource_MIReturn_param =
{
    MI_FLAG_PARAMETER|MI_FLAG_OUT, /* flags */
    0x006D6E08, /* code */
    MI_T("MIReturn"), /* name */
    MSFT_nxOMSPerfCounterResource_SetTargetResource_MIReturn_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_SetTargetResource_MIReturn_quals), /* numQualifiers */
    MI_UINT32, /* type */
    NULL, /* className */
    0, /* subscript */
    offsetof(MSFT_nxOMSPerfCounterResource_SetTargetResource, MIReturn), /* offset */
};

static MI_ParameterDecl MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_SetTargetResource_params[] =
{
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_MIReturn_param,
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_InputResource_param,
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_ProviderContext_param,
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_Flags_param,
};

/* method MSFT_nxOMSPerfCounterResource.SetTargetResource() */
MI_CONST MI_MethodDecl MSFT_nxOMSPerfCounterResource_SetTargetResource_rtti =
{
    MI_FLAG_METHOD|MI_FLAG_STATIC, /* flags */
    0x00736511, /* code */
    MI_T("SetTargetResource"), /* name */
    MSFT_nxOMSPerfCounterResource_SetTargetResource_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_SetTargetResource_quals), /* numQualifiers */
    MSFT_nxOMSPerfCounterResource_SetTargetResource_params, /* parameters */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_SetTargetResource_params), /* numParameters */
    sizeof(MSFT_nxOMSPerfCounterResource_SetTargetResource), /* size */
    MI_UINT32, /* returnType */
    MI_T("MSFT_nxOMSPerfCounterResource"), /* origin */
    MI_T("MSFT_nxOMSPerfCounterResource"), /* propagator */
    &schemaDecl, /* schema */
    (MI_ProviderFT_Invoke)MSFT_nxOMSPerfCounterResource_Invoke_SetTargetResource, /* method */
};

static MI_MethodDecl MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_meths[] =
{
    &MSFT_nxOMSPerfCounterResource_GetTargetResource_rtti,
    &MSFT_nxOMSPerfCounterResource_TestTargetResource_rtti,
    &MSFT_nxOMSPerfCounterResource_SetTargetResource_rtti,
};

static MI_CONST MI_ProviderFT MSFT_nxOMSPerfCounterResource_funcs =
{
  (MI_ProviderFT_Load)MSFT_nxOMSPerfCounterResource_Load,
  (MI_ProviderFT_Unload)MSFT_nxOMSPerfCounterResource_Unload,
  (MI_ProviderFT_GetInstance)MSFT_nxOMSPerfCounterResource_GetInstance,
  (MI_ProviderFT_EnumerateInstances)MSFT_nxOMSPerfCounterResource_EnumerateInstances,
  (MI_ProviderFT_CreateInstance)MSFT_nxOMSPerfCounterResource_CreateInstance,
  (MI_ProviderFT_ModifyInstance)MSFT_nxOMSPerfCounterResource_ModifyInstance,
  (MI_ProviderFT_DeleteInstance)MSFT_nxOMSPerfCounterResource_DeleteInstance,
  (MI_ProviderFT_AssociatorInstances)NULL,
  (MI_ProviderFT_ReferenceInstances)NULL,
  (MI_ProviderFT_EnableIndications)NULL,
  (MI_ProviderFT_DisableIndications)NULL,
  (MI_ProviderFT_Subscribe)NULL,
  (MI_ProviderFT_Unsubscribe)NULL,
  (MI_ProviderFT_Invoke)NULL,
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterResource_Description_qual_value = MI_T("1");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_Description_qual =
{
    MI_T("Description"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_TOSUBCLASS|MI_FLAG_TRANSLATABLE,
    &MSFT_nxOMSPerfCounterResource_Description_qual_value
};

static MI_CONST MI_Char* MSFT_nxOMSPerfCounterResource_ClassVersion_qual_value = MI_T("1.0.0");

static MI_CONST MI_Qualifier MSFT_nxOMSPerfCounterResource_ClassVersion_qual =
{
    MI_T("ClassVersion"),
    MI_STRING,
    MI_FLAG_ENABLEOVERRIDE|MI_FLAG_RESTRICTED,
    &MSFT_nxOMSPerfCounterResource_ClassVersion_qual_value
};

static MI_Qualifier MI_CONST* MI_CONST MSFT_nxOMSPerfCounterResource_quals[] =
{
    &MSFT_nxOMSPerfCounterResource_Description_qual,
    &MSFT_nxOMSPerfCounterResource_ClassVersion_qual,
};

/* class MSFT_nxOMSPerfCounterResource */
MI_CONST MI_ClassDecl MSFT_nxOMSPerfCounterResource_rtti =
{
    MI_FLAG_CLASS, /* flags */
    0x006D651D, /* code */
    MI_T("MSFT_nxOMSPerfCounterResource"), /* name */
    MSFT_nxOMSPerfCounterResource_quals, /* qualifiers */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_quals), /* numQualifiers */
    MSFT_nxOMSPerfCounterResource_props, /* properties */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_props), /* numProperties */
    sizeof(MSFT_nxOMSPerfCounterResource), /* size */
    MI_T("OMI_BaseResource"), /* superClass */
    &OMI_BaseResource_rtti, /* superClassDecl */
    MSFT_nxOMSPerfCounterResource_meths, /* methods */
    MI_COUNT(MSFT_nxOMSPerfCounterResource_meths), /* numMethods */
    &schemaDecl, /* schema */
    &MSFT_nxOMSPerfCounterResource_funcs, /* functions */
    NULL /* owningClass */
};

/*
**==============================================================================
**
** __mi_server
**
**==============================================================================
*/

MI_Server* __mi_server;
/*
**==============================================================================
**
** Schema
**
**==============================================================================
*/

static MI_ClassDecl MI_CONST* MI_CONST classes[] =
{
    &MSFT_nxOMSPerfCounterObject_rtti,
    &MSFT_nxOMSPerfCounterResource_rtti,
    &OMI_BaseResource_rtti,
};

MI_SchemaDecl schemaDecl =
{
    qualifierDecls, /* qualifierDecls */
    MI_COUNT(qualifierDecls), /* numQualifierDecls */
    classes, /* classDecls */
    MI_COUNT(classes), /* classDecls */
};

/*
**==============================================================================
**
** MI_Server Methods
**
**==============================================================================
*/

MI_Result MI_CALL MI_Server_GetVersion(
    MI_Uint32* version){
    return __mi_server->serverFT->GetVersion(version);
}

MI_Result MI_CALL MI_Server_GetSystemName(
    const MI_Char** systemName)
{
    return __mi_server->serverFT->GetSystemName(systemName);
}

