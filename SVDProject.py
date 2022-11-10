'''Student Fair use Statement'''
'''Copyright Disclaimer under section 107 of the Copyright Act 1976, allowance is made for “fair use” for purposes such as criticism, comment, news reporting, teaching, scholarship, education and research. Fair use is a use permitted by copyright statute that might otherwise be infringing.'''

'''Singular Value Decomposition (SVD) 
    Data Reduction
    Data-Driven Generalization of fourien transform (FFT)
    "Tailored" to specific problem
   
    APPLICATIONS:
    SVD can solve Ax = b ==> for non square A
    Regression
    basis for Principal Component Analysis (PCA) (Takes high demensional data and understand based on correlation and most important key features
   
    REAL WORLD APPLICATIONS: 
    Google Search Algorithm
    Facebook Face identity Algorithm
    Amazon and Netflix recommenders
    
    Simple/interretable Linear Algebra
    
    Data matrix X 
    X = U * S (Sigma) * Vt (V transposed T)
    
    Code modified from Data Driven Science and Engineering by: Steven Brunton and Nathan Kutz

    '''
'''Image sources'''
'''Eye image source:
https://cdn.britannica.com/79/150179-050-E2707D87/human-eye.jpg'''
'''Helix Nevula image source: 
https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNV-kyCm9tvCT2ruH5H3lLQWEKAjmcYs9Yr-GgGx9sDhZ8K7wfB-0_YUFfSK-jWWmGp44&usqp=CAU'''


from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np 
import os
def convert_bw(picture):
    '''Converts the image to bw'''
    plt.rcParams['figure.figsize'] = [4,3]##Sets image size in pixels *100

    A = imread(picture)## Reads image
    X = np.mean(A, -1)##Converts image to RGB

    ## Shows the image
    img = plt.imshow(X)
    img.set_cmap('gray')
    plt.axis('off')
    plt.show()
    return X

def make_svd(X):
    U, S, VT = np.linalg.svd(X,full_matrices=False) ##Decomposes the image into sub matrices
    S = np.diag(S) ## Computsed the sigma or diagonal matrix

    ## Generates a rank 2 decompostion to compare images at
    j = 0
    r = 2
    # Builds compressed imaged based on the decompostion of sub matrices
    Xapprox = U[:,:r] @ S[0:r,:r] @ VT[:r,:]
    plt.figure(j+1)
    j += 1
    ## Shows compressed image with title of decompositon level
    img = plt.imshow(Xapprox)
    img.set_cmap('gray')
    plt.axis('off')
    plt.title('r = ' + str(r))
    plt.show()

    ## repeated decompositons of rank 5, 20, and 100
    for r in (5, 20, 100):
        # Construct approximate image
        Aapprox = U[:,:r] @ S[0:r,:r] @ VT[:r,:]
        plt.figure(j+1)
        j += 1
        img = plt.imshow(Aapprox)
        img.set_cmap('gray')
        plt.axis('off')
        plt.title('r = ' + str(r))
        plt.show()

    ## Return value is only the matrix of the rank 2 decomposition
    return Xapprox

def main():
    usi1 = input("Enter a name: ")
    output1 = (make_svd(convert_bw(usi1)))
    usi2 = input("Enter a name: ")
    output2 = (make_svd(convert_bw(usi2)))
    similar = {}

    ##Image similarity test comparing trace values of rank 2 matrices
    trace1 = output1.trace()
    trace2 = output2.trace()
    print(f"The trace of value of image1 is: {trace1}")
    print(f"The trace of vlaue of image2 is: {trace2}")
    if trace1 == trace2:
        print("These images are the same")
        similar[usi1] = usi2
    else:
        print("These images are not the same.")
    ##Image similarity could be tested further I am unsure of how image size, color, pixel density changes similarity at this point.
    '''Images used were of a human Eye and a Helix nebula. 
    Examining the intersection betwen art and sceince both the eye and helix nebula can leave us asking more questions such as how similar are these images.
    What does perspective tell us about the environment around us.'''
    

main()
