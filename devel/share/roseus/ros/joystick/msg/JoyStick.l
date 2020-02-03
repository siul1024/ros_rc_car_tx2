;; Auto-generated. Do not edit!


(when (boundp 'joystick::JoyStick)
  (if (not (find-package "JOYSTICK"))
    (make-package "JOYSTICK"))
  (shadow 'JoyStick (find-package "JOYSTICK")))
(unless (find-package "JOYSTICK::JOYSTICK")
  (make-package "JOYSTICK::JOYSTICK"))

(in-package "ROS")
;;//! \htmlinclude JoyStick.msg.html


(defclass joystick::JoyStick
  :super ros::object
  :slots (_steering _throttle ))

(defmethod joystick::JoyStick
  (:init
   (&key
    ((:steering __steering) 0.0)
    ((:throttle __throttle) 0.0)
    )
   (send-super :init)
   (setq _steering (float __steering))
   (setq _throttle (float __throttle))
   self)
  (:steering
   (&optional __steering)
   (if __steering (setq _steering __steering)) _steering)
  (:throttle
   (&optional __throttle)
   (if __throttle (setq _throttle __throttle)) _throttle)
  (:serialization-length
   ()
   (+
    ;; float32 _steering
    4
    ;; float32 _throttle
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _steering
       (sys::poke _steering (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _throttle
       (sys::poke _throttle (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _steering
     (setq _steering (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _throttle
     (setq _throttle (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get joystick::JoyStick :md5sum-) "07077f1ca3b57b112f69aabcdabf600e")
(setf (get joystick::JoyStick :datatype-) "joystick/JoyStick")
(setf (get joystick::JoyStick :definition-)
      "float32 steering
float32 throttle

")



(provide :joystick/JoyStick "07077f1ca3b57b112f69aabcdabf600e")


