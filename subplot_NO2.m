[X1,map1]=imread('EGYPT_June_08_2020.png');
[X2,map2]=imread('EGYPT_June_07_June_08_2020.png');
[X3,map3]=imread('EGYPT_June_07_2020.png');
[X4,map4]=imread('EGYPT_June_05_June_06_2020.png');
[X5,map5]=imread('EGYPT_June_07_June_08_2020__diff.png');
[X6,map6]=imread('EGYPT_June_05to06_June_07to08__2020__diff.png');

subplot_tight(3,2,1, [0.05 0.05]), imshow(X1,map1), title('June 08, 2020')  
subplot_tight(3,2,2, [0.05 0.05]), imshow(X2,map2), title('Average of June 07 and June 08, 2020') 
subplot_tight(3,2,3, [0.05 0.05]), imshow(X3,map3), title('June 07, 2020') 
subplot_tight(3,2,4, [0.05 0.05]), imshow(X4,map4), title('Average of June 05 and June 06, 2020') 
subplot_tight(3,2,5, [0.05 0.05]), imshow(X5,map5), title('Difference') 
subplot_tight(3,2,6, [0.05 0.05]), imshow(X6,map6), title('Difference') 

sdf('NO2');  
saveas(gcf,'EGYPT.png')
clf;


[X1,map1]=imread('EGYPT_June_08_2020.png');
[X2,map2]=imread('EGYPT_June_07_June_08_2020.png');
[X3,map3]=imread('EGYPT_June_07_2020.png');
[X4,map4]=imread('EGYPT_June_05_June_06_2020.png');
[X5,map5]=imread('EGYPT_June_07_June_08_2020__diff.png');
[X6,map6]=imread('EGYPT_June_05to06_June_07to08__2020__diff.png');

subplot_tight(3,2,1, [0.05 0.05]), imshow(X1,map1), title('June 08, 2020')  
subplot_tight(3,2,2, [0.05 0.05]), imshow(X2,map2), title('Average of June 07 and June 08, 2020') 
subplot_tight(3,2,3, [0.05 0.05]), imshow(X3,map3), title('June 07, 2020') 
subplot_tight(3,2,4, [0.05 0.05]), imshow(X4,map4), title('Average of June 05 and June 06, 2020') 
subplot_tight(3,2,5, [0.05 0.05]), imshow(X5,map5), title('Difference') 
subplot_tight(3,2,6, [0.05 0.05]), imshow(X6,map6), title('Difference') 

sdf('NO2');  
saveas(gcf,'EGYPT.png')
clf;

