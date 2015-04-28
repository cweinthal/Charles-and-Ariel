% error analysis
%input locations: 
R=[4,4];%robot location

C=[-1,-1,9,9,-1,9,9,-1]; %camera location
a=sqrt((R(1)-C(1))^2+(R(2)-C(5))^2);
b=sqrt((R(1)-C(2))^2+(R(2)-C(6))^2);
c=sqrt((R(1)-C(3))^2+(R(2)-C(7))^2);
d=sqrt((R(1)-C(4))^2+(R(2)-C(8))^2);
v1=[C(2),C(6)]-[C(1),C(5)];
v2=R-[C(1),C(5)];
angle1=acos(dot(v1,v2)/(norm(v1)*norm(v2)));
v1=[C(3),C(7)]-[C(2),C(6)];
v2=R-[C(2),C(6)];
angle2=acos(dot(v1,v2)/(norm(v1)*norm(v2)));
v1=[C(4),C(8)]-[C(3),C(7)];
v2=R-[C(3),C(7)];
angle3=acos(dot(v1,v2)/(norm(v1)*norm(v2)));
v1=[C(1),C(5)]-[C(4),C(8)];
v2=R-[C(4),C(8)];
angle4=acos(dot(v1,v2)/(norm(v1)*norm(v2)));

% summerize:
C=[-1,-1,9,9,-1,9,9,-1]; %camera location
%actual distancen and angle with respect to four cameras 
D=[a,b,c,d]
A=[angle1*180/pi,angle2*180/pi,angle3*180/pi,angle4*180/pi]
% add some error for the distance. the farther, the larger error
a_e=randi([-round(a),round(a)]); 
b_e=randi([-round(b),round(b)]); 
c_e=randi([-round(c),round(c)]); 
d_e=randi([-round(d),round(d)]); 
D_e=[a+0.01*a_e,b+0.01*b_e,c+0.01*c_e,d+0.01*d_e]
%estimated location from calculation:
 x1=-1+D_e(1)*sind(A(1)); y1=-1+D_e(1)*cosd(A(1));
 x2=-1+D_e(2)*cosd(A(2));y2=9-D_e(2)*sind(A(2));
 x3=9-D_e(3)*sind(A(3));y3=9-D_e(3)*cosd(A(3));
 x4=9-D_e(4)*cosd(A(4));y4=-1+D_e(4)*sind(A(4));
 R_x=[x1,x2,x3,x4]
 R_y=[y1,y2,y3,y4]
e_p=[sqrt((x1-R(1))^2+(y1-R(2))^2)/sqrt(R(1)^2+R(2)^2),sqrt((x2-R(1))^2+(y2-R(2))^2)/sqrt(R(1)^2+R(2)^2),sqrt((x3-R(1))^2+(y3-R(2))^2)/sqrt(R(1)^2+R(2)^2),sqrt((x4-R(1))^2+(y4-R(2))^2)/sqrt(R(1)^2+R(2)^2)]
