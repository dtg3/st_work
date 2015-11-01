import unittest
import nypl_search, nypl_responsive, nypl_view

class Test_000_Search(nypl_search.NYPLSearch):
	pass

class Test_001_View(nypl_view.NYPLView):
	pass

class Test_002_Responsive(nypl_responsive.NYPLResponsive):
	pass

if __name__ == "__main__":
    unittest.main()
