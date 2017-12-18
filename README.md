Nap_Zap : A Search Engine Using Python
=============================================
This Project is about creating a web search engine using python :
This project meets the following criteria:
  1. Collect HTML pages up to a maximum size.(according to given crawl-depth)
  2. Make a pre-processing on these pages (eliminate 'stop words')
  3. Index crawled data.
  4. Submitting queries and returning the result
  5. Display the result in an appropriate order of relevance.
  6. A web interface!
  
  #Requirements
  See requirements.txt


  # Structure
  
  1. indexes: A directory of indexed web-pages by Indexer.py
     * forward_index :  Forward indexing
     * inverted_index : Inverted indexing
     * url_to_id : For mapping indexed urls.
  2. links :  A directory of web-pages crawled by Crawler.py
            
      A web-pages(url) crawled and saved offline in links 
      directory and named with base64 encoding.
      (To store longest urls in distinct names.)
  3. static : A directory of static(logo) files like pictures.
   
  4. templates : A directory of views (front-end files).
  
  5. Crawler.py : Main Crawler module
       
       To Run Crawler.py
                
                $python Crawler.py --start_url "url" --max_depth depth_value
       
       url : website address that you want to crawl.
       depth_value: Maximum depth of crawl (integer)
  
       * if this will get completed successfully it will run indexer.py itself , if not then follow
       next to run indexer.py module.
       
       * By default all crawled data will be stored in 'links/' directory.
  6. indexer.py : Main Indexer Module
  
       To Run indexer.py
       
                $python indexer.py --stored_docs_dir links/ --index_dir indexes
       
       * this module require to arguments 
        1. stored link's directory (to generate index)
        2. index directory (to store generated index)
       
       * if this will get completed successfully then it will run web_ui.py itself.
  7. web_ui.py : Frontend (view)
  
       To run web_ui.py
       
                $python web_ui.py
       * it will start at [0.0.0.0:8080](http://0.0.0.0:8080/)
  8. lang_proc.py : Language Processing Module
      
  9. util.py : HTML parser Module


###### Currently 2 websites crawled
    1.wikipedia.org (Crawl_Depth-1)
    2.Python.org (Crawl_Depth-3)