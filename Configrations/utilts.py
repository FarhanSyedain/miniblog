from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    
    
    def get_paginated_response(self, data):
        
        total_objs = self.page.paginator.count
        objes_per_count = self.get_page_size(self.request)
        page = self.page.number
        
        #Check Number of pages-- if total_objs // objes_per_count, as an int , is equal to itself as a float , then we have posts equally spread 
        #through the pages, consequently we have total_objs // objes_per_count pages ; otherwisw we have one page with unequal posts and rest pages have equal number of posts.
        if total_objs // objes_per_count == total_objs / objes_per_count:
            total_pages = int(total_objs // objes_per_count )
        else:
            total_pages = int(total_objs // objes_per_count + 1)
        
        pages_back = []
    
        #check pages before current page
        if page == 2:
            pages_back = [1]
        elif page >= 3:
            pages_back  = [i for i in range(page-2,page)]

        #all pages after current page
        pages_forth = [i for i in range(page+1,total_pages+1)]#All the pages forth
    
        try:
            pages_forth = pages_forth[0:2] # Get the next two pages
        except IndexError:#If we have less than 2 pages
            pages_forth = pages_forth 
                   
        return Response({
            'results': data,
            'paginator':{
                'pages_forth':pages_forth,
                'pages_back':pages_back,
                'current_page':page,
            }
        })