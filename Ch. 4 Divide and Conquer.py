## Here is the plot of land problem. You have a plot of land and you need to 
## figure out how to divide the land into the largest SQUARE plots as possible.

## Divide & Conquer is not a simple algorithm that you can aapply to a problem.
## Instead, its a way to think about a problem. 

def largestPlots(long, short):
    if long % short != 0:
        plots = int(long/short)
        long = short
        short = plots
        print(long, short)
        largestPlots(long, short)
    else:
        print(f"We have a solution! {short} by {short}")
    
  
print(largestPlots(100,15))

