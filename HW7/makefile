Python = python
Viewer = less

.Phony = run view clean

run: prob1

prob1 : set.py test-set.py
	$(Python) test-set.py

view : set.py
	$(Viewer) set.py

clean : 
	rm *.pyc 
