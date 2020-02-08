// Auto-generated. Do not edit!

// (in-package joystick.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class JoyStick {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.steering = null;
      this.throttle = null;
      this.brk_status = null;
      this.rec_status = null;
    }
    else {
      if (initObj.hasOwnProperty('steering')) {
        this.steering = initObj.steering
      }
      else {
        this.steering = 0.0;
      }
      if (initObj.hasOwnProperty('throttle')) {
        this.throttle = initObj.throttle
      }
      else {
        this.throttle = 0.0;
      }
      if (initObj.hasOwnProperty('brk_status')) {
        this.brk_status = initObj.brk_status
      }
      else {
        this.brk_status = false;
      }
      if (initObj.hasOwnProperty('rec_status')) {
        this.rec_status = initObj.rec_status
      }
      else {
        this.rec_status = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type JoyStick
    // Serialize message field [steering]
    bufferOffset = _serializer.float32(obj.steering, buffer, bufferOffset);
    // Serialize message field [throttle]
    bufferOffset = _serializer.float32(obj.throttle, buffer, bufferOffset);
    // Serialize message field [brk_status]
    bufferOffset = _serializer.bool(obj.brk_status, buffer, bufferOffset);
    // Serialize message field [rec_status]
    bufferOffset = _serializer.bool(obj.rec_status, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type JoyStick
    let len;
    let data = new JoyStick(null);
    // Deserialize message field [steering]
    data.steering = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [throttle]
    data.throttle = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [brk_status]
    data.brk_status = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [rec_status]
    data.rec_status = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 10;
  }

  static datatype() {
    // Returns string type for a message object
    return 'joystick/JoyStick';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '529be6a2e8574e4ce2287a2d5c8ed377';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 steering
    float32 throttle
    bool brk_status
    bool rec_status
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new JoyStick(null);
    if (msg.steering !== undefined) {
      resolved.steering = msg.steering;
    }
    else {
      resolved.steering = 0.0
    }

    if (msg.throttle !== undefined) {
      resolved.throttle = msg.throttle;
    }
    else {
      resolved.throttle = 0.0
    }

    if (msg.brk_status !== undefined) {
      resolved.brk_status = msg.brk_status;
    }
    else {
      resolved.brk_status = false
    }

    if (msg.rec_status !== undefined) {
      resolved.rec_status = msg.rec_status;
    }
    else {
      resolved.rec_status = false
    }

    return resolved;
    }
};

module.exports = JoyStick;
