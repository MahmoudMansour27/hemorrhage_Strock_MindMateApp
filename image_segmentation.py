# segmentaion function
from skimage.segmentation import slic, mark_boundaries, chan_vese
from skimage import img_as_float, filters
import matplotlib.pyplot as plt
import cv2

path = 'test_case.jpg'

# ct-scan image
def unsupervised_segmentation(path):
    case = cv2.imread(path)
    
    astr_segments = slic(case, n_segments=70, compactness=1)
    
    plt.subplot(1, 2, 1)
    plt.title("Orignal CT-Scan")
    plt.imshow(case)
    
    plt.subplot(1, 2, 2)
    plt.title("Segmented CT-Scan")
    plt.imshow(mark_boundaries(case, astr_segments))
    
    plt.tight_layout()
    
    # save result to be used in report
    plt.savefig('temp_saves/unsupervised_segmentation.png')
    print('image has been saved')
    
    plt.show()
    

    
def chan_vese_segmentation(path):
    case = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    case_chan_vese = chan_vese(case, max_num_iter=200, extended_output=True)
    
    #orginal 
    plt.subplot(1, 3, 1)
    plt.title("Orignal CT-Scan")
    plt.imshow(case, cmap= 'gray')
    
    # 100 iteration
    plt.subplot(1, 3, 2)
    plt.title("Segmented 10 Iter")
    plt.imshow(case_chan_vese[0], cmap= 'gray')
    
    # final level set
    plt.subplot(1, 3, 3)
    plt.title("Final Level Set")
    plt.imshow(case_chan_vese[1], cmap= 'gray')
    
    plt.tight_layout()
    
    
    # save result to be used in report
    plt.savefig('temp_saves/chan_vese_segmentation.png')
    print('image has been saved')
    
    plt.show()
    

def hsv(path):
    case = cv2.imread(path)
    case_rgb = cv2.cvtColor(case, cv2.COLOR_BGR2RGB)
    case_hsv = cv2.cvtColor(case, cv2.COLOR_BGR2HSV)
    
    plt.subplot(1, 2, 1)
    plt.title("Orignal CT-Scan")
    plt.imshow(case_rgb)
    
    plt.subplot(1, 2, 2)
    plt.title("HSV CT-Scane")
    plt.imshow(case_hsv)
    
    plt.tight_layout()
    
    
    # save result to be used in report
    plt.savefig('temp_saves/hsv.png')
    print('image has been saved')
    
    plt.show()
    
 
def supervised_segmentation(path):
    case = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    
    plt.subplot(2, 3, 1)
    plt.title("Orignal CT-Scan")
    plt.imshow(case, cmap='gray')
    
    plot_num = 2
    for thresh in range(120, 161, 10):
        _, binary=cv2.threshold(case,thresh,255,cv2.THRESH_BINARY)
        plt.subplot(2, 3, plot_num)
        plt.title(f"Threshold {thresh}")
        plt.imshow(binary, cmap='gray')
        plot_num += 1
    
    plt.tight_layout()
      
    # save result to be used in report
    plt.savefig('temp_saves/supervised_segmentation.png')
    print('image has been saved')
    
    plt.show()
    
    
def Adaptive_thresh(path):

    case = cv2.imread(path)
    case = cv2.cvtColor(case, cv2.COLOR_BGR2GRAY)
    
    plt.subplot(1, 3, 1)
    plt.title("Orignal CT-Scan")
    plt.imshow(case, cmap = 'gray')
    
    mean_adaptive = cv2.adaptiveThreshold(case, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 199, 5)
    plt.subplot(1, 3, 2)
    plt.title("Adaptive Mean")
    plt.imshow(mean_adaptive,cmap='gray')

    gaussian_adaptive = cv2.adaptiveThreshold(case, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 199, 5)
    plt.subplot(1, 3, 3)
    plt.title("Adaptive Gausssian")
    plt.imshow(gaussian_adaptive,cmap="gray")
    
    plt.tight_layout()
    
    # save result to be used in report
    plt.savefig('temp_saves/Adaptive_thresh.png')
    print('image has been saved')
    
    plt.show()
    
# unsupervised_segmentation(path)
# chan_vese_segmentation(path)
# hsv(path)
# supervised_segmentation(path)
# Adaptive_thresh(path)

