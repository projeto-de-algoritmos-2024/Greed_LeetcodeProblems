# Questão Média 1090. Largest Values From Labels - Algoritmo de Huffman
class Solution(object):
    def largestValsFromLabels(self, values, labels, numWanted, useLimit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type numWanted: int
        :type useLimit: int
        :rtype: int
        """
        items = list(zip(values, labels))
        
        items.sort(key=lambda x: x[0], reverse=True)

        label_count = {}
        total_value = 0
        items_used = 0

        for value, label in items:
            if items_used >= numWanted:
                break

            if label_count.get(label, 0) < useLimit:
                total_value += value
                items_used += 1
                label_count[label] = label_count.get(label, 0) + 1

        return total_value

solution = Solution()

values = [5, 4, 3, 2, 1]
labels = [1, 1, 2, 2, 3]
numWanted = 3
useLimit = 1
print("Output Exemplo 1:", solution.largestValsFromLabels(values, labels, numWanted, useLimit))

values = [5, 4, 3, 2, 1]
labels = [1, 3, 3, 3, 2]
numWanted = 3
useLimit = 2
print("Output Exemplo 2:", solution.largestValsFromLabels(values, labels, numWanted, useLimit))

values = [9, 8, 8, 7, 6]
labels = [0, 0, 0, 1, 1]
numWanted = 3
useLimit = 1
print("Output Exemplo 3:", solution.largestValsFromLabels(values, labels, numWanted, useLimit))