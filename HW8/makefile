Python = python
Viewer = less
Input_File = my.input

.Phony = run view clean

run: prob1

prob1 : floyd.py
	$(Python) floyd.py $(Input_File)

view : floyd.py
	$(Viewer) floyd.py

clean : 
	rm *.pyc 
