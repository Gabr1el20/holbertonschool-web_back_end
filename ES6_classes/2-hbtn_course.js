export default class HolbertonCourse {
  constructor(name = '', length = 0, students = []) {
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
    if (typeof (listStudents) === 'object') {
      for (const student in listStudents) {
        if (typeof (student) !== 'string') {
          throw new TypeError('Students must be an array of strings');
        }
      }
    } else {
      throw new TypeError('Students must be an array of strings!');
    }
    this._students = listStudents;
  }
}
