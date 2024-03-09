# index_creation.py
# Purpose is to run the corpus and create the inverted index to store in the DB

import runner, mongo, page_rank


def main():
    inverted_index = runner.InvertedIndex()
    # inverted_index.run_and_extract()

    page_ranks = inverted_index.get_page_rank_urls()
    inverted_index.sort_by_page_rank(page_ranks)
    # inverted_index.sort_by_page_rank(page_ranks)
    #page_rank.compute_page_rank(inverted_index.links)
    
    
        
    # mongo.prepare_documents_for_insertion(inverted_index.inverted_index)
    # mongo.calculate_idf_from_mongo()

if __name__ == "__main__":
    main()