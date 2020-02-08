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
  :slots (_steering _throttle _brk_status _rec_status ))

(defmethod joystick::JoyStick
  (:init
   (&key
    ((:steering __steering) 0.0)
    ((:throttle __throttle) 0.0)
    ((:brk_status __brk_status) nil)
    ((:rec_status __rec_status) nil)
    )
   (send-super :init)
   (setq _steering (float __steering))
   (setq _throttle (float __throttle))
   (setq _brk_status __brk_status)
   (setq _rec_status __rec_status)
   self)
  (:steering
   (&optional __steering)
   (if __steering (setq _steering __steering)) _steering)
  (:throttle
   (&optional __throttle)
   (if __throttle (setq _throttle __throttle)) _throttle)
  (:brk_status
   (&optional __brk_status)
   (if __brk_status (setq _brk_status __brk_status)) _brk_status)
  (:rec_status
   (&optional __rec_status)
   (if __rec_status (setq _rec_status __rec_status)) _rec_status)
  (:serialization-length
   ()
   (+
    ;; float32 _steering
    4
    ;; float32 _throttle
    4
    ;; bool _brk_status
    1
    ;; bool _rec_status
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
     ;; bool _brk_status
       (if _brk_status (write-byte -1 s) (write-byte 0 s))
     ;; bool _rec_status
       (if _rec_status (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _steering
     (setq _steering (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _throttle
     (setq _throttle (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; bool _brk_status
     (setq _brk_status (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _rec_status
     (setq _rec_status (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get joystick::JoyStick :md5sum-) "529be6a2e8574e4ce2287a2d5c8ed377")
(setf (get joystick::JoyStick :datatype-) "joystick/JoyStick")
(setf (get joystick::JoyStick :definition-)
      "float32 steering
float32 throttle
bool brk_status
bool rec_status
")



(provide :joystick/JoyStick "529be6a2e8574e4ce2287a2d5c8ed377")


