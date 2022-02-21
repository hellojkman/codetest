main :
	python3 test.py < test.in > result.out
	
test :
	python3 test.py < test.in > result.out
	diff test.out result.out