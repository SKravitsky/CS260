Python = python
Viewer = less

.Phony = run view

run: problem1 problem2 problem3 view

problem1 : problem1.py
	$(Python) problem1.py

problem2 : problem2.py
	$(Python) problem2.py

problem3 : problem3.py
	$(Python) problem3.py

view : problem1.py problem2.py problem3.py
	$(Viewer) problem1.py problem2.py problem3.py 
