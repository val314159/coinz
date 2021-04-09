all:
	@echo type "valid targets are: clean realclean"
clean:
	find . -name '*~' | xargs rm -fr
	tree .
realclean: clean
update: realclean
	git add .
	git commit -am update
	git push
