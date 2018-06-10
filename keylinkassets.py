import itertools

class KeyLinkAssets:

    letterLowerCaseList = ['a', 'b', 'c', 'd', 'e', 'f',
                                'g', 'h', 'i', 'j', 'k', 'l',
                                     'm', 'n', 'o', 'p', 'q', 'r',
                                          's', 't', 'u', 'v', 'w', 'x',
                                               'y', 'z']


    letterUpperCaseList = ['A', 'B', 'C', 'D', 'E', 'F',
                                    'G', 'H', 'I', 'J', 'K', 'L',
                                        'M', 'N', 'O', 'P', 'Q', 'R',
                                            'S', 'T', 'U', 'V', 'X', 'X',
                                                'Y', 'Z']   

    numberList =['1', '2', '3', '4', '5' , '6', '7', '8', '9', '0']                                      


    extraCharList = ['!' , '"',  '#',  '$', '%',  '&', "'", '(',  ')', '*', '+', ',' , '-', '.', '/',  '[', '\\', '_', "`", "{", '|', "}", "~", "]", '^' ]

    @staticmethod
    def createLinkAssets():

        linkedAssets = []

        linkedAssets.extend(KeyLinkAssets.letterLowerCaseList)

        linkedAssets.extend(KeyLinkAssets. letterUpperCaseList )

        linkedAssets.extend(KeyLinkAssets.numberList)

        linkedAssets.extend(KeyLinkAssets.extraCharList)


        return linkedAssets