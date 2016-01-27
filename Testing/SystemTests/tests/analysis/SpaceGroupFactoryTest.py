# pylint: disable=no-init
import stresstesting
import re
from mantid.simpleapi import *
from mantid.geometry import *


class SpaceGroupFactoryTest(stresstesting.MantidStressTest):
    '''Check that the space groups generated by Mantid are correct.'''

    spaceGroupData = None
    notChecked = []

    def runTest(self):
        self.spaceGroupData = self.loadReferenceData()

        availableSpaceGroups = SpaceGroupFactory.getAllSpaceGroupSymbols()

        self.notChecked = []

        for symbol in availableSpaceGroups:
            self.checkSpaceGroup(symbol)

        # There are some space groups which have new names in the latest tables, they will be included in the
        # test when aliases are available.
        self.assertLess(len(self.notChecked), 25,
                        'Some space groups were not checked: ' + str(self.notChecked))

    def checkSpaceGroup(self, symbol):
        group = SpaceGroupFactory.createSpaceGroup(symbol)

        self.checkPointGroupOfSpaceGroup(group)

        self.assertTrue(group.isGroup(),
                        ("Space group " + str(group.getNumber()) + " (" + symbol + ") does not "
                                                                                   "fulfill group axioms"))

        groupOperations = set(group.getSymmetryOperationStrings())

        if symbol in self.spaceGroupData:
            referenceOperations = self.spaceGroupData[symbol]

            differenceOne = groupOperations - referenceOperations
            differenceTwo = referenceOperations - groupOperations

            self.assertTrue(len(differenceOne) == 0,
                            "Problem in space group " + str(group.getNumber()) + " (" + symbol + ")")
            self.assertTrue(len(differenceTwo) == 0,
                            "Problem in space group " + str(group.getNumber()) + " (" + symbol + ")")
            self.assertTrue(groupOperations == referenceOperations,
                            "Problem in space group " + str(group.getNumber()) + " (" + symbol + ")")
        else:
            self.notChecked.append((group.getNumber(), symbol))

    def checkPointGroupOfSpaceGroup(self, spaceGroup):
        # Get all space group operations, remove translations - resulting group is the point group
        allOperations = spaceGroup.getSymmetryOperationStrings()
        translationMatcher = re.compile(r"(\-|\+)(\d\/\d)")
        onlyMatrices = Group(';'.join([translationMatcher.sub('', x) for x in allOperations]))

        pointGroup = spaceGroup.getPointGroup()

        self.assertFalse(
                set(onlyMatrices.getSymmetryOperationStrings()).isdisjoint(pointGroup.getSymmetryOperationStrings()),
                ("Point group of space group " + spaceGroup.getHMSymbol() + " does not match group obtained from"
                                                                            " matrices of symmetry operations."))

    def loadReferenceData(self):
        # Reference data, generated using sginfo (http://cci.lbl.gov/sginfo/)
        # Dictionary has a string set of symmetry operation identifiers for each space group number.
        separatorMatcher = re.compile(r"# (.+)")

        fileName = FileFinder.Instance().getFullPath('SpaceGroupSymmetryOperations.txt')

        fileHandle = open(fileName, 'r')
        spaceGroups = {}
        for currentLine in fileHandle:
            matchedSeparator = separatorMatcher.match(currentLine)

            if matchedSeparator is not None:
                currentGroup = matchedSeparator.group(1)

                print currentGroup

                spaceGroups[currentGroup] = set()
            else:
                spaceGroups[currentGroup].add(
                        SymmetryOperationFactory.createSymOp(currentLine.strip()).getIdentifier())

        return spaceGroups
