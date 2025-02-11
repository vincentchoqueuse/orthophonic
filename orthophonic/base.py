import numpy as np


class Vector:
    """
    A class representing a mathematical vector with various operations.

    Attributes
    ----------
    array : np.ndarray
        The underlying array storing vector elements.
    """
    
    def __init__(self, data):
        """
        Initialize the vector.

        Parameters
        ----------
        data : int, list, or np.ndarray
            - If `data` is an integer or float, use an array of size 1
            - If `data` is a list or np.ndarray, uses it as the vector content.

        Raises
        ------
        ValueError
            If the input data type is invalid.
        """
        if isinstance(data, (int, float, np.int64, np.float32)):
            self.array = np.array([data], dtype=float)
        elif isinstance(data, (list, np.ndarray)):
            self.array = np.array(data, dtype=float)
        else:
            raise ValueError("Invalid input. Provide an integer for size or a list/array-like for content.")

    def astype(self, dtype):
        """
        Convert the vector elements to the specified data type.

        Parameters
        ----------
        dtype : type
            The desired data type (e.g., np.float32, np.int32).
        """
        self.array = self.array.astype(dtype)
        return self
    
    def clear(self):
        """
        Reset the vector to all zeros.
        """
        self.array = np.zeros(len(self.array))
        return self
    
    def multiply(self, scalar):
        """
        Mutliply the vector elements by a scalar.
        
        Parameters
        ----------
        scalar : float
            The scaling factor.
        """
        self.array *= scalar
        return self
    
    def add(self, offset):
        """
        Offset the vector elements by a scalar.
        
        Parameters
        ----------
        offset : float
            The value to add to each element.
        """
        self.array += offset
        return self
    
    def reverse(self):
        """
        Reverse the elements of the vector.
        """
        self.array = self.array[::-1]
        return self

    def direct_sum(self, data):
        """
        Direct sum with a vector
        """
        array1 = self.array
        array2 = self.get_array(data)
        array = np.kron(array1, np.ones(len(array2))) + np.kron(np.ones(len(array1)), array2)
        return Vector(array)
    
    def set_value(self, pos, value):
        """
        Set a specific value in the vector.
        
        Parameters
        ----------
        pos : int
            The index where the value should be set.
        value : float
            The value to set.
        """
        self.array[pos] = value
        return self
    
    def rvs_normal(self, loc=0, scale=1):
        """
        Add normally distributed random noise to the vector.

        Parameters
        ----------
        loc : float, optional
            Mean of the normal distribution (default is 0).
        scale : float, optional
            Standard deviation of the normal distribution (default is 1).
        """
        self.array += np.random.normal(loc=loc, scale=scale, size=len(self.array))
        return self
    
    def roll(self, shift):
        """
        Roll (circular shift) the vector elements by a specified amount.
        
        Parameters
        ----------
        shift : int
            The number of positions to shift the elements.
        """
        self.array = np.roll(self.array, shift)
        return self
    
    def repeat(self, times):
        """
        Replicate the content of the vector `times` times.

        Parameters
        ----------
        times : int
            The number of times to repeat the vector.

        Raises
        ------
        ValueError
            If `times` is less than 1.
        """
        if times < 1:
            raise ValueError("Number of times to replicate must be at least 1.")
        self.array = np.tile(self.array, times)
        return self
    
    def clip(self, min_value=0, max_value=127):
        """
        Clip the vector's values to be within the range [min_value, max_value].

        Parameters
        ----------
        min_value : float, optional
            Minimum allowed value (default is 0).
        max_value : float, optional
            Maximum allowed value (default is 127).
        """
        self.array = np.clip(self.array, min_value, max_value)
        return self

    def project(self, data, scale=0):
        """
        Project the vector into the nearest element of data.

        Parameters
        ----------
        data : list, Vector
            The alphabet 
        scale : float, optional
            the hardness of projection (0: hard projection, 1: no projection)
        """
        grid = self.get_array(data)
        grid = np.insert(grid, 0, 0)
        array_before = self.array
        array_hard = grid[np.argmin(np.abs(array_before[:, None] - grid), axis=1)]
        self.array = array_before*scale + (1-scale)*array_hard
        return self

    def resize(self, length):
        """
        Resize a vector to a specific length by using repetition

        Parameters
        ----------
        length: integer

        """
        self.array = np.resize(self.array, length)
        return self


    def get_array(self, data):
        """
        Return an array from data

        Parameters
        ----------
        data: list, Vector, np.array

        """

        if isinstance(data, Vector):
            output = data.array
        if isinstance(data, np.ndarray):
            output = data
        if isinstance(data, list):
            output = np.array(data)

        return output

    
    def tolist(self):
        """
        Convert the vector to a Python list.
        """
        return self.array.tolist()
    
    def __len__(self):
        """
        Return the length of the vector.
        """
        return len(self.array)
    
    def __getitem__(self, index):
        """
        Retrieve an element by index.
        """
        return self.array[index]
    
    def __repr__(self):
        """
        Return a string representation of the vector.
        """
        return f"Vector({self.array.tolist()})"


class Sine_Zeros(Vector):
    """
    A subclass of `Vector` representing zero crossings of a sine wave.
    
    Parameters
    ----------
    M : int
        The number of zero crossings in the period.
    N : int
        The total number of points in the period.
    theta : float, optional
        Phase shift of the sine wave (default is 0).
    repeat : int, optional
        Number of times to repeat the pattern (default is 1).
    """
    def __init__(self, M, N, theta=0, repeat=1):
        M = repeat * M
        N = repeat * N
        m = np.arange(M)
        array = m * N / M - theta
        super().__init__(array)
