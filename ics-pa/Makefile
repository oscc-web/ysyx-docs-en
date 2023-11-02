SRC_PATH = ./
BOOK_PATH = ./_book
PUBLISH_PATH = ../publish/ics2023

run:
	gitbook serve $(SRC_PATH)

web: clean
	gitbook build $(SRC_PATH) #--log=debug --debug
	# Fix links for the offline version. See https://github.com/NJU-ProjectN/ics-pa-gitbook/issues/5
	#sed -i -e 's/if(m)for(n.handler/if(false)for(n.handler/' $(BOOK_PATH)/gitbook/theme.js
	ls $(BOOK_PATH)/*.html | xargs sed -i -e 's+"./"+"index.html"+'

pdf:
	gitbook pdf $(SRC_PATH)

init:
	gitbook install
	sed -i -r 's/<h3>/<h5>/' node_modules/gitbook-plugin-callouts/index.js

publish: web
	-rm -r $(PUBLISH_PATH)
	cp -r $(BOOK_PATH) $(PUBLISH_PATH)
	cd $(PUBLISH_PATH) && git add . && git commit --amend -m "first commit"

clean:
	rm -r $(BOOK_PATH)
