This is not intended as a working, installable package. It's a subtree of the
`src/` folder of the private `graflipy` package intended as a rough trailmap
of how we tooled some EGA metadata operations.

The main takeaway should be that it's not too difficult:

1. use the EGA/SRA XSD to autogenerate some python dataclasses that model the schema
1. write some methods to map your database results to dataclass instances
1. serialize to XML
1. upload the XML to EGA via the REST API
1. bin/prepare_data.sh file is not the subtree for the Python tools code
