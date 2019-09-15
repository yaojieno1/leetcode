class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        if (l1 + l2) == 0:
            return 0
        elif l1 == 0:
            med_ind = self.get_med_index(l2)
            return self.get_med_value_for_1_array(med_ind, [], -1, -1, nums2)
        elif l2 == 0:
            med_ind = self.get_med_index(l1)
            return self.get_med_value_for_1_array(med_ind, [], -1, -1, nums1)

        med_ind = self.get_med_index(l1 + l2)
        return self.get_indexed_value_from_2_array(med_ind, nums1, nums2)

    def get_med_value_for_1_array(self, med_ind, med_val, t, i, arr):
        if len(med_val) == 1:
            return (arr[med_ind[0] + i - t] + med_val[0]) / 2.0
        elif len(med_ind) == 1:
            return arr[med_ind[0] + i - t]
        else:
            return (arr[med_ind[0] + i - t] + arr[med_ind[1] + i - t]) / 2.0

    def get_med_index(self, tot_len):
        med_ind = []
        if tot_len == 0:
            med_ind.append(0)
            return med_ind
        if tot_len % 2 == 0:
            med_ind.append(tot_len / 2 - 1)
            med_ind.append(tot_len / 2)
        else:
            med_ind.append(tot_len / 2)
        return med_ind

    def get_ava_val(self, med_val):
        l = len(med_val)
        if l == 0:
            return -1
        if l == 1:
            return med_val[0]
        if l == 2:
            return (med_val[0] + med_val[1]) / 2.0
        return -2

    def check(self, val, t, med_ind, med_val):
        if t != med_ind[0]:
            return
        med_val.append(val)
        med_ind.remove(med_ind[0])

    def get_indexed_value_from_2_array(self, med_ind, nums1, nums2):
        i = 0
        j = 0
        t = -1
        med_val = []
        while True:
            t = t + 1
            if nums1[i] <= nums2[j]:
                self.check(nums1[i], t, med_ind, med_val)
                i = i + 1
            elif nums1[i] > nums2[j]:
                self.check(nums2[j], t, med_ind, med_val)
                j = j + 1
            if len(med_ind) == 0:
                return self.get_ava_val(med_val)
            if i >= len(nums1):
                return self.get_med_value_for_1_array(med_ind, med_val, t + 1, j, nums2)
            if j >= len(nums2):
                return self.get_med_value_for_1_array(med_ind, med_val, t + 1, i, nums1)
