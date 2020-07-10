class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        tam = {y:i for i,y in enumerate(list1)}
        print (tam)
        k1 = 100000
        dem={}
        for i,y in enumerate(list2):
            if y in tam:
                dem[y]=i+tam[y]
                k1 = min(k1,dem[y])
        return [res for res, s in dem.items() if s==k1]

        