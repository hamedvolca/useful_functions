function [center,radius] = create_circle_from_three_points(a,plot_flag)
    % create_circle_from_three_points(a,false)
    % a = rand(2,3); three points in the form of  2x3 matrix
    % plot_flag: false -> no plot, true -> plot the circle
    % 
    % The code does check the collinearity.
    % If three points are not distinct, collinearity is detected.
    % The code does NOT check the size and type of the inputs.

    pointsAreCollinear = @(xy) rank(xy(2:end,:) - xy(1,:)) == 1;
    if pointsAreCollinear(a')
        disp('Collinear points')
        center = false;
        radius = false;
    else
        [temp, order] = sort(a(2,:));
        a_sorted_1 = a(:,order);
        
        p1 = a_sorted_1(:,3);

        a_sorted = a_sorted_1;
        a_sorted(:,3)=[];
        [temp, order] = sort(a_sorted(1,:));
        a_sorted = a_sorted(:,order);

        p2 = a_sorted(:,2);
        p3 = a_sorted(:,1);
        
        v1 = (p2-p1)/2;
        v2 = (p3-p2)/2;
        v1_p = [v1(2),-v1(1)]';
  
        x1 = v1(1);
        y1 = v1(2);
        x2 = v2(1);
        y2 = v2(2);
        
        m1 = x1 * x2 + x2 * x2 + y1 * y2 + y2 * y2;
        m2 = y1 * x2 - x1 * y2;
        mu = m1/m2;
        c = p1 + v1 + mu * v1_p;

        center = c;
        radius = norm(c-p1);
        if plot_flag
            figure();
            hold on
            scatter(p1(1),p1(2),'red')
            scatter(p2(1),p2(2),'b')
            scatter(p3(1),p3(2),'k')
            scatter(c(1),c(2),'black','+')
           
            plot([p1(1)+v1(1),center(1)],[p1(2)+v1(2), center(2)],'k-.')
            plot([p2(1)+v2(1),center(1)],[p2(2)+v2(2), center(2)],'k-.')
            circle(c(1),c(2),norm(c-p1))
            plot([p1(1),p2(1)],[p1(2),p2(2)],'b')
            plot([p2(1),p3(1)],[p2(2),p3(2)],'b')
            axis equal
            
        end
    end
    
    function h = circle(x,y,r)
        th = 0:pi/50:2*pi;
        xunit = r * cos(th) + x;
        yunit = r * sin(th) + y;
        h = plot(xunit, yunit);
    end
end
