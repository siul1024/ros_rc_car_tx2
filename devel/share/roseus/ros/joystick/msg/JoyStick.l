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
  :slots (_steering _throttle _brake ))

(defmethod joystick::JoyStick
  (:init
   (&key
    ((:steering __steering) 0.0)
    ((:throttle __throttle) 0.0)
    ((:brake __brake) nil)
    )
   (send-super :init)
   (setq _steering (float __steering))
   (setq _throttle (float __throttle))
   (setq _brake __brake)
   self)
  (:steering
   (&optional __steering)
   (if __steering (setq _steering __steering)) _steering)
  (:throttle
   (&optional __throttle)
   (if __throttle (setq _throttle __throttle)) _throttle)
  (:brake
   (&optional __brake)
   (if __brake (setq _brake __brake)) _brake)
  (:serialization-length
   ()
   (+
    ;; float32 _steering
    4
    ;; float32 _throttle
    4
    ;; bool _brake
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _steering
       (sys::poke _steering (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _throttle
       (sys::poke _throttle (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; bool _brake
       (if _brake (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _steering
     (setq _steering (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _throttle
     (setq _throttle (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; bool _brake
     (setq _brake (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get joystick::JoyStick :md5sum-) "74d0717dbec8219b6d54e7c43afb3fa6")
(setf (get joystick::JoyStick :datatype-) "joystick/JoyStick")
(setf (get joystick::JoyStick :definition-)
      "float32 steering
float32 throttle
bool brake

")



(provide :joystick/JoyStick "74d0717dbec8219b6d54e7c43afb3fa6")


