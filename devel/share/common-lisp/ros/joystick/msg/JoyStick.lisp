; Auto-generated. Do not edit!


(cl:in-package joystick-msg)


;//! \htmlinclude JoyStick.msg.html

(cl:defclass <JoyStick> (roslisp-msg-protocol:ros-message)
  ((steering
    :reader steering
    :initarg :steering
    :type cl:float
    :initform 0.0)
   (throttle
    :reader throttle
    :initarg :throttle
    :type cl:float
    :initform 0.0))
)

(cl:defclass JoyStick (<JoyStick>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <JoyStick>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'JoyStick)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name joystick-msg:<JoyStick> is deprecated: use joystick-msg:JoyStick instead.")))

(cl:ensure-generic-function 'steering-val :lambda-list '(m))
(cl:defmethod steering-val ((m <JoyStick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader joystick-msg:steering-val is deprecated.  Use joystick-msg:steering instead.")
  (steering m))

(cl:ensure-generic-function 'throttle-val :lambda-list '(m))
(cl:defmethod throttle-val ((m <JoyStick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader joystick-msg:throttle-val is deprecated.  Use joystick-msg:throttle instead.")
  (throttle m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <JoyStick>) ostream)
  "Serializes a message object of type '<JoyStick>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'steering))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'throttle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <JoyStick>) istream)
  "Deserializes a message object of type '<JoyStick>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'steering) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'throttle) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<JoyStick>)))
  "Returns string type for a message object of type '<JoyStick>"
  "joystick/JoyStick")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'JoyStick)))
  "Returns string type for a message object of type 'JoyStick"
  "joystick/JoyStick")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<JoyStick>)))
  "Returns md5sum for a message object of type '<JoyStick>"
  "07077f1ca3b57b112f69aabcdabf600e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'JoyStick)))
  "Returns md5sum for a message object of type 'JoyStick"
  "07077f1ca3b57b112f69aabcdabf600e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<JoyStick>)))
  "Returns full string definition for message of type '<JoyStick>"
  (cl:format cl:nil "float32 steering~%float32 throttle~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'JoyStick)))
  "Returns full string definition for message of type 'JoyStick"
  (cl:format cl:nil "float32 steering~%float32 throttle~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <JoyStick>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <JoyStick>))
  "Converts a ROS message object to a list"
  (cl:list 'JoyStick
    (cl:cons ':steering (steering msg))
    (cl:cons ':throttle (throttle msg))
))
