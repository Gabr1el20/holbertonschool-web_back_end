export default function cleanSet(aSet, startString) {
  if (startString === '') return '';
  const filteredValues = Array.from(aSet)
    .filter((value) => value.startsWith(startString))
    .map((value) => value.substring(startString.length));
  return filteredValues.join('-');
}
