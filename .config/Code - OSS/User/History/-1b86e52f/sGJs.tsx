interface ContainerProps {
  children: React.ReactNode;
}

const Container: React.FC<ContainerProps> = ({ children }) => {
  return <div className="max-w-[2520] mx-auto ">{children}</div>;
};

export default Container;
