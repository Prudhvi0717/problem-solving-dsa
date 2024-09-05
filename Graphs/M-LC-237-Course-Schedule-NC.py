## link: https://leetcode.com/problems/course-schedule/description/

class Solution:
    """
    We create a adjacency list to represent these prerequisites as graph
    If there is a cycle we cant complete that course.

    If we reach a course which has no prerequisites, it means the course can be completed.
    For all courses which can be completed we make the prereqs = []
    So that we dont have to dfs on that course again later.

    We perform dfs on each course and perform optimzations like emptying each course's prereqs
    so that we dont perform the same again later.

    We maintain a visit set to track cycles.
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## adjacency list
        preMap = {n : [] for n in range(numCourses)}

        ## map each course to its prerequisites
        for course, pre in prerequisites:
            preMap[course].append(pre)

        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            preMap[crs] = []
            visitSet.remove(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

