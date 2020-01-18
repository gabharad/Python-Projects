import cv2
import datetime as dt

cap = cv2.VideoCapture('vtest.avi');
print(cap.get(3))
print(cap.get(4))

#cap.set(3, 500)
#cap.set(4, 500)
#print(cap.get(3))
#print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: '+ str(cap.get(3)) + ' Height: ' + str(cap.get(4))
        dtime =str(dt.datetime.now())
        frame =cv2.putText(frame, dtime, (10,50), font, 1, (0,255,255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()