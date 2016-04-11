clear;
n=10;
m=100
lambda1=0.05;
lambda2=0.03;
k1=1;
k2=1;
Hun=log2(n);
[T, H] = meshgrid(1:1:100, 0:Hun/100:Hun);
Nun=(1-exp(-lambda1*T)).*(m-(m-1)*H/Hun);
C=4*n*(H/Hun).^4+ m*T.^-1
P=Nun*k1+C*k2;
surf(T,H,P)