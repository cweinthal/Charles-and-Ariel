clc;clf;clear all
theta=15:0.01:75;
d=0.75*8*sqrt(2);
offset =0.5
x0=-1-offset
y0=9+offset

%(x0,x0)
x=d*cosd(theta)+x0;
y=d*sind(theta)+x0;
plot(x,y,'Color','red')
hold on
line([x0,d*sind(75)+x0],[x0,d*cosd(75)+x0],'Color','r')
x1=x0;x2=d*sind(75)+x0;y1=x0;y2=d*cosd(75)+x0;
line([x0,d*sind(15)+x0],[x0,d*cosd(15)+x0],'Color','red')

%(y0,x0)
theta=105:0.01:165;
x=d*cosd(theta)+y0;
y=d*sind(theta)+x0;
plot(x,y,'Color','g')
line([y0,-d*sind(165)+y0],[x0,-d*cosd(165)+x0],'Color','g') 
x3=y0;x4=-d*sind(105)+y0;y3=x0;y4=-d*cosd(105)+x0;
line([y0,-d*sind(105)+y0],[x0,-d*cosd(105)+x0],'Color','g')



%(y0,y0)
theta=195:0.01:255;
x=d*cosd(theta)+y0;
y=d*sind(theta)+y0;
plot(x,y,'Color','k')
line([y0,-d*sind(75)+y0],[y0,-d*cosd(75)+y0],'Color','k')
line([y0,-d*sind(15)+y0],[y0,-d*cosd(15)+y0],'Color','k')

%(x0,y0)
theta=-75:0.01:-15;
x=d*cosd(theta)+x0;
y=d*sind(theta)+y0;
plot(x,y,'Color','m')
line([x0,d*sind(75)+x0],[y0,-d*cosd(75)+y0],'Color','m')
line([x0,d*sind(15)+x0],[y0,-d*cosd(15)+y0],'Color','m')

%Plot the results 
line([x0,x0],[x0,y0],'LineWidth',2)
hold on
line([x0,y0],[y0,y0],'LineWidth',2)
line([y0,y0],[y0,x0],'LineWidth',2)
line([y0,x0],[x0,x0],'LineWidth',2)
line([0,0],[0,8])
line([0,8],[8,8])
line([8,8],[8,0])
line([8,0],[0,0])
axis([-2,10,-2,10])
axis equal


%calculate the area 
k1=(y2-y1)/(x2-x1);
k2=(y4-y3)/(x4-x3);
b1=y1-k1*x1;
b2=y3-k2*x3;
% syms u v
[solx,soly]=solve('k1*u+b1==v','k2*u+b2==v')
[solxx,solyy]=solve('k2*u+b2==v','v==0')
h=-(b1*k2 - b2*k1)/(k1 - k2)

area=((-b2/k2)-(-b1/k1))*0.5*h
coverrate=(1-4*area/64)*100 % cover rate %



