import time, types, string
from atop import store

# Index classes
class CategoryIndex(store.StringIndex):
    """Each Lo is indexed for searching by category."""

class KeywordIndex(store.StringIndex):
    """Each Lo is indexed for searching by keywords."""

#DublinCore Indexes, see dublincore.org

class TitleIndex(store.StringIndex):
    """ 
Definition:     A name given to the resource.
Comment:        Typically, Title will be a name by which the resource is 
                formally known.    
    """
    
class CreatorIndex(store.StringIndex):
    """ 
Definition:     An entity primarily responsible for making the content of the 
                resource.
Comment:        Examples of Creator include a person, an organization, or a 
                service. Typically, the name of a Creator should be used to 
                indicate the entity.    
    """

class SubjectIndex(store.StringIndex):
    """ 
Definition:     A topic of the content of the resource.
Comment:        Typically, Subject will be expressed as keywords, key phrases 
                or classification codes that describe a topic of the resource. 
                Recommended best practice is to select a value from a 
                controlled vocabulary or formal classification scheme.    
    """

class DescriptionIndex(store.StringIndex):
    """ 
Definition:     An account of the content of the resource.
Comment:        Examples of Description include, but is not limited to: an 
                abstract, table of contents, reference to a graphical 
                representation of content or a free-text account of the 
                content.    
    """

class PublisherIndex(store.StringIndex):
    """ 
Definition:     An entity responsible for making the resource available
Comment:        Examples of Publisher include a person, an organization, 
                or a service. Typically, the name of a Publisher should 
                be used to indicate the entity.     
    """

class ContributorIndex(store.StringIndex):
    """ 
Definition:     An entity responsible for making contributions to the 
                content of the resource.
Comment:        Examples of Contributor include a person, an organization, or 
                a service. Typically, the name of a Contributor should be used 
                to indicate the entity.    
    """

class DateIndex(store.StringIndex):
    """ 
Definition:     A date of an event in the lifecycle of the resource.
Comment:        Typically, Date will be associated with the creation or 
                availability of the resource. Recommended best practice for 
                encoding the date value is defined in a profile of ISO 8601 
                [W3CDTF] and includes (among others) dates of the form 
                YYYY-MM-DD.    
    """

class TypeIndex(store.StringIndex):
    """ 
Definition:     The nature or genre of the content of the resource.
Comment:        Type includes terms describing general categories, functions, 
                genres, or aggregation levels for content. Recommended best 
                practice is to select a value from a controlled vocabulary 
                (for example, the DCMI Type Vocabulary [DCT1]). To describe 
                the physical or digital manifestation of the resource, use the 
                FORMAT element.    
    """

class FormatIndex(store.StringIndex):
    """ 
Definition:     The physical or digital manifestation of the resource.
Comment:        Typically, Format may include the media-type or dimensions of 
                the resource. Format may be used to identify the software, 
                hardware, or other equipment needed to display or operate the
                resource. Examples of dimensions include size and duration. 
                Recommended best practice is to select a value from a 
                controlled vocabulary (for example, the list of Internet Media
                Types [MIME] defining computer media formats).    
    """

class IdentifierIndex(store.StringIndex):
    """ 
Definition:     An unambiguous reference to the resource within a given context.
Comment:        Recommended best practice is to identify the resource by means 
                of a string or number conforming to a formal identification 
                system. Formal identification systems include but are not 
                limited to the Uniform Resource Identifier (URI) (including the 
                Uniform Resource Locator (URL)), the Digital Object Identifier 
                (DOI) and the International Standard Book Number (ISBN).    
    """

class SourceIndex(store.StringIndex):
    """ 
Definition:     A Reference to a resource from which the present resource is 
                derived.
Comment:        The present resource may be derived from the Source resource 
                in whole or in part. Recommended best practice is to identify 
                the referenced resource by means of a string or number 
                conforming to a formal identification system.    
    """

class LanguageIndex(store.StringIndex):
    """ 
Definition:     A language of the intellectual content of the resource.
Comment:        Recommended best practice is to use RFC 3066 [RFC3066] which, 
                in conjunction with ISO639 [ISO639]), defines two- and 
                three-letter primary language tags with optional subtags. 
                Examples include "en" or "eng" for English, "akk" for 
                Akkadian", and "en-GB" for English used in the United Kingdom.    
    """

class RelationIndex(store.StringIndex):
    """ 
Definition:     A reference to a related resource.
Comment:        Recommended best practice is to identify the referenced 
                resource by means of a string or number conforming to a formal 
                identification system.    
    """

class CoverageIndex(store.StringIndex):
    """ 
Label:  Coverage
Definition:     The extent or scope of the content of the resource.
Comment:        Typically, Coverage will include spatial location (a place 
                name or geographic coordinates), temporal period (a period 
                label, date, or date range) or jurisdiction (such as a named 
                administrative entity). Recommended best practice is to 
                select a value from a controlled vocabulary (for example, 
                the Thesaurus of Geographic Names [TGN]) and to use, where 
                appropriate, named places or time periods in preference to 
                numeric identifiers such as sets of coordinates or date 
                ranges.    
    """

class RightsIndex(store.StringIndex):
    """ 
Label:  Rights Management
Definition:     Information about rights held in and over the resource.
Comment:        Typically, Rights will contain a rights management statement 
                for the resource, or reference a service providing such 
                information. Rights information often encompasses Intellectual 
                Property Rights (IPR), Copyright, and various Property Rights. 
                If the Rights element is absent, no assumptions may be made 
                about any rights held in or over the resource.    
    """


LoIndexes = [CategoryIndex, CreationDateIndex, KeywordIndex]

#Learning Objects

class LoBase(store.Item):
    """The base class for all Learning Objects."""
    
    _categories = store.indexedList(CategoryIndex)
    _keywords = store.indexedList(KeywordIndex)
    
    #see dublincore.org, dublincore is the metadata standard.
    dublinCore_Title       = store.indexed(TitleIndex)
    dublinCore_Creator     = store.indexed(CreatorIndex)
    dublinCore_Subject     = store.indexed(SubjectIndex)
    dublinCore_Description = store.indexed(DescriptionIndex)
    dublinCore_Publisher   = store.indexed(PublisherIndex)
    dublinCore_Contributor = store.indexed(ContributorIndex)
    dublinCore_Date        = store.indexed(DateIndex)
    dublinCore_Type        = store.indexed(TypeIndex)
    dublinCore_Format      = store.indexed(FormatIndex)
    dublinCore_Identifier  = store.indexed(IdentifierIndex)
    dublinCore_Source      = store.indexed(SourceIndex)
    dublinCore_Language    = store.indexed(LanguageIndex)
    dublinCore_Relation    = store.indexed(RelationIndex)
    dublinCore_Coverage    = store.indexed(CoverageIndex)
    dublinCore_Rights      = store.indexed(RightsIndex)

   
    def __init__(self, st):
        store.Item.__init__(self, st)
        self.dublinCore_Date = time.time()
        self._categories = []

    def categorise(self, categories):
        """Assign this lo to some categories."""
        assert type(categories) is types.ListType
        self._categories = categories
        
    def setKeywords(self, keywords):
        """Assign this lo some keywords."""
        assert type(keywords) is types.ListType
        #lowercased for searching
        self._keywords = \
            [string.lower(string.strip(k,string.punctuation)) for k in keywords]

class LoText(LoBase):
    """An lo that comprises of formatted text."""
    
    def __init__(self, store, categories):
        LoBase.__init__(self, store)
        self.categorise(categories)
        self.text = ""

    def setText(self, text):
        self.text = text
        self.setKeywords(self.text.split())

class LoConstruct(LoBase):
    """An lo that is constructed of other lo's."""
    
    def __init__(self, store):
        LoBase.__init__(self, store)
        self.content = {}
        

class LoImage(LoBase):
    """An lo that contains an image."""
    
    def __init__(self, store):
        LoBase.__init__(self, store)
        self.image = None
        self.caption = None
        self.height = None
        self.width = None
