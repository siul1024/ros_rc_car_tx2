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
    :initform 0.0)
   (brk_status
    :reader brk_status
    :initarg :brk_status
    :type cl:boolean
    :initform cl:nil)
   (rec_status
    :reader rec_status
    :initarg :rec_status
    :type cl:boolean
    :initform cl:nil))
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

(cl:ensure-generic-function 'brk_status-val :lambda-list '(m))
(cl:defmethod brk_status-val ((m <JoyStick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader joystick-msg:brk_status-val is deprecated.  Use joystick-msg:brk_status instead.")
  (brk_status m))

(cl:ensure-generic-function 'rec_status-val :lambda-list '(m))
(cl:defmethod rec_status-val ((m <JoyStick>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader joystick-msg:rec_status-val is deprecated.  Use joystick-msg:rec_status instead.")
  (rec_status m))
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
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'brk_status) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'rec_status) 1 0)) ostream)
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
    (cl:setf (cl:slot-value msg 'brk_status) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'rec_status) (cl:not (cl:zerop (cl:read-byte istream))))
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
  "529be6a2e8574e4ce2287a2d5c8ed377")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'JoyStick)))
  "Returns md5sum for a message object of type 'JoyStick"
  "529be6a2e8574e4ce2287a2d5c8ed377")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<JoyStick>)))
  "Returns full string definition for message of type '<JoyStick>"
  (cl:format cl:nil "float32 steering~%float32 throttle~%bool brk_status~%bool rec_status~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'JoyStick)))
  "Returns full string definition for message of type 'JoyStick"
  (cl:format cl:nil "float32 steering~%float32 throttle~%bool brk_status~%bool rec_status~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <JoyStick>))
  (cl:+ 0
     4
     4
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <JoyStick>))
  "Converts a ROS message object to a list"
  (cl:list 'JoyStick
    (cl:cons ':steering (steering msg))
    (cl:cons ':throttle (throttle msg))
    (cl:cons ':brk_status (brk_status msg))
    (cl:cons ':rec_status (rec_status msg))
))
