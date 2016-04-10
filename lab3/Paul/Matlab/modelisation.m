clear;
n=10;
m=100
lambda1=0.05;
lambda2=0.03;
k1=1;
k2=1;
Hun=log2(n);
[T, H] = meshgrid(0:1:100, 0:Hun/100:Hun);
Nun=(1-exp(-lambda1*T)).*(m-(m-1)*H/Hun);
C=(1+(n-1)*(2*H/Hun).^2)+ 4*n*exp(-lambda2*T)
P=Nun*k1+C*k2;
surf(T,H,P)