export default class HolbertonCourse {
  constructor(name = '', length = 0, students = []) {
    if (typeof (name) !== 'string') {
      throw TypeError('name must be an string');
    }
    if (typeof (length) !== 'number') {
      throw TypeError('length must be a number');
    }
    if (students.some((element) => (typeof (element) !== 'string'))) {
      throw TypeError('students must be an array of strings');
    }
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof (value) === 'string') {
      this._name = value;
    }
  }

  get length() {
    return this._length;
  }

  set length(value) {
    if (typeof (value) === 'number') {
      this._length = value;
    }
  }

  get students() {
    return this._students;
  }

  set students(listStudents) {
    if (listStudents.some((element) => (typeof (element) !== 'string'))) {
      throw TypeError('students must be an array of strings');
    }
    this._students = listStudents;
  }
}
