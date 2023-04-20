export default function Input() {
  return (
    <div className="relative">
      <input
        id="email"
        className="block rounded-md px-6 pt-6 pb-1 w-full text-md text-white bg-neutral-700 appearance-none focus:outline-none focus:ring-0 peer"
        placeholder=" "
      />
      <label
        className="absolute text-md text-zinc-400 duration-150 transform -translate-y-3"
        htmlFor="email"
      ></label>
    </div>
  );
}
