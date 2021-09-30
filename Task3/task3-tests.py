import subgraph_gen


# Insert test functions here

def testGetDistance():
    assert subgraph_gen.getStraightLineDistance([0,0],[3,4]) == 5, "Should be 5"

# Insert test functions here under here to run when this python script is run.
if __name__ == "__main__":

    # Run all test fuctions
    testGetDistance()
    ## End of test functions

    print("All test has passed")