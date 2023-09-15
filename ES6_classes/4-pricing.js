import Currency from './3-currency.js';

export default class Pricing {
  constructor(amount = 0, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  set amount(value) {
    this._amount = value;
  }

  displayFullPrice() {
    const code = (this.currency._code);
    const name = (this.currency._name);
    const money = `${this.amount} ${name} ${code})`;

    return money;
  }

  static convertPrice(amount = 0, conversionRate = 0) {
    if (typeof (conversionRate) !== 'number') {
      throw new TypeError('conversionRate must be a number');
    }
    if (typeof (amount) !== 'number') {
      throw new TypeError('amount must be a number');
    }
    return (amount * conversionRate);
  }

  set currency(value) {
    this._currency = value;
  }

  get amount() {
    return this._amount;
  }

  get currency() {
    return this._currency;
  }
}
