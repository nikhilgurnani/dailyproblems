"""
You are given a hash table where the key is a course code, and the value is a list of all the course codes that are prerequisites for the key. Return a valid ordering in which we can complete the courses. If no such ordering exists, return NULL.

Example:
{
  'CSC300': ['CSC100', 'CSC200'],
  'CSC200': ['CSC100'],
  'CSC100': []
}

This input should return the order that we need to take these courses:
 ['CSC100', 'CSC200', 'CSCS300']
"""

final_map = {}
final = []
def courses_to_take(course_to_prereqs):

    for key in course_to_prereqs:
        for pre_req in course_to_prereqs[key]:

    if final_map.get( key, None) is None:
        final.append( key )
        final_map.update({ key: True })




courses = {
    'CSC300': ['CSC100', 'CSC200'],
    'CSC200': ['CSC100'],
    'CSC100': [],
    'CSC400': ['CSC100', 'CSC200', 'CSC300']
}
courses_to_take(courses, 'CSC300')

print( final )
# ['CSC100', 'CSC200', 'CSC300']
