commit:
	@echo "Running git on octave_backend"
	git add -A
	git commit -m $(COMMENT)
	git push origin master
	cd "$(PWD)/frontend" && make commit $(COMMENT)
