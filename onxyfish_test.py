#!/usr/bin/env python

from sunburnt import SolrInterface
from sunburnt.search import SolrSearch

solr = SolrInterface('http://localhost:8983/solr')
s = SolrSearch(solr)

print 'Testing basic query'

response = s.query(full_text='Education').execute()

print response.result

print 'Testing group query'

response = s.query(full_text='Education').group_by('dataset_id', limit=2).execute()

for k, g in response.result.groups.items():
    print k, g.docs 
