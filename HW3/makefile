Python = python
Viewer = less
GP = gnuplot
Plotter = plot-instructions

.Phony = run problem1 problem2 problem 3 clean view

run: problem1 problem2 problem3

problem1 : problem1.py
	$(Python) problem1.py $(arg)

problem2 : problem2.py
	$(Python) problem2.py $(arg)

problem3 : problem3.py
	$(Python) problem3.py
	$(GP) $(Plotter)

view : problem1.py problem2.py problem3.py
	$(Viewer) problem1.py problem2.py problem3.py

clean : 
	rm mydata.txt
	rm plot.png
	rm *.pyc 
