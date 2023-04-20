import { BiCheck } from "react-icons/bi";

type TypeProps = {
  message: string;
};

export default function Success({ message }: TypeProps) {
  return (
    <div className="success container mx-auto">
      <div className="flex justify-center mx-auto border border-[#bf616a] bg-[#bf616a] w-3/6 text-[#bf616a] text-md my-4 py-2 text-center bg-opacity-5">
        {message} <BiCheck size={25} color={"#a3be8c"} />
      </div>
    </div>
  );
}
