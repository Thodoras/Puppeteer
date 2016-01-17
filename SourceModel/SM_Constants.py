CLASS_REGEX = r'class \w+(?:\:\:\w+)*\s*(?:\(.+\)\s*)*{*'
DEFINE_REGEX = r'define \w+(?:\:\:\w+)*\s*(?:\(.+\)\s*)*{*'
FILE_REGEX = r'file\W*\{\W*\'.+\'\W*:|file\W*\{\W*\".+\"\W*:|file\W*{\W*\$.+\W*:'
PACKAGE_REGEX = r'package\W*\{\W*\'.+\'\W*:|package\W*\{\W*\".+\"\W*:|package\W*{\W*\$.+\W*:'
SERVICE_REGEX = r'service\W*\{\W*\'.+\'\W*:|service\W*\{\W*\".+\"\W*:|service\W*{\W*\$.+\W*:'
EXEC_REGEX = r'exec\W*\{\W*\'.+\'\W*:|exec\W*\{\W*\".+\"\W*:|exec\W*{\W*\$.+\W*:'
LOC_REGEX = r'\n'
IF_REGEX = r'if\W+.+\W*\{'
CASE_REGEX = r'case\W+.+\W*\{'
USER_REGEX = r'user\W*\{\W*.+:'
COMMENT_REGEX = r'\A#|\n#'
HARDCODED_VALUE_REGEX = r'= \d+|=> \d+|= .*\'.+?\s*(?:\(.+\)\s*)*\'|=> .*\'.+?\s*(?:\(.+\)\s*)*\'|' \
                        r'= .*\".+?\s*(?:\(.+\)\s*)*\"|=> .*\".+\s*(?:\(.+\)\s*)*\"'

CLASS_GROUP_REGEX = r'class (\w+(?:\:\:\w+)*)\s*(?:\(.+\)\s*)*{*'
CLASS_INH_REGEX = r'inherits (\w+(?:\:\:\w+)*){*'
FILE_GROUP_REGEX = r'file\W*\{\W*\'(.+)\'\W*:|file\W*\{\W*\"(.+)\"\W*:|file\W*{\W*(\$.+)\W*:'
PACKAGE_GROUP_REGEX = r'package\W*\{\W*\'(.+)\'\W*:|package\W*\{\W*\"(.+)\"\W*:|package\W*{\W*(\$.+)\W*:'
SERVICE_GROUP_REGEX = r'service\W*\{\W*\'(.+)\'\W*:|service\W*\{\W*\"(.+)\"\W*:|service\W*{\W*(\$.+)\W*:'

DEPENDENT_PACKAGE = r'Package\W*\[\'.+\'\]'
DEPENDENT_SERVICE = r'Service\W*\[\'.+\'\]'
DEPENDENT_FILE = r'File\W*\[\'.+\'\]'
DEPENDENT_CLASS = r'Class\W*\[\'.+\'\]'

DEPENDENT_GROUP_PACKAGE = r'Package\W*\[\'(.+)\'\]'
DEPENDENT_GROUP_SERVICE = r'Service\W*\[\'(.+)\'\]'
DEPENDENT_GROUP_FILE = r'File\W*\[\'(.+)\'\]'
DEPENDENT_GROUP_CLASS = r'Class\W*\[\'(.+)\'\]'

PACKAGE = "Package"
FILE = "File"
SERVICE = "Service"
CLASS = "Class"

VAR1_REGEX = r'\$\{.+\}'
VAR2_REGEX = r'\$.+\W*\{'
VAR3_REGEX = r'\'.+\''
VAR4_REGEX = r'\".+\"'

VAR1_EX_REGEX = r'\$\{(.+)\}'
VAR2_EX_REGEX = r'\$(.+)\W*\{'
VAR3_EX_REGEX = r'\'(.+)\''
VAR4_EX_REGEX = r'\"(.+)\"'
#class\W+.+\{|
