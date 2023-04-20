interface ContainerProps {
  children: React.ReactNode;
}

const Container: React.FC<ContainerProps> = ({ children }) => {
  return (
    <div className="max-w-[2520] mx-auto xl:px-20 md:px-10">{children}</div>
  );
};

export default Container;
