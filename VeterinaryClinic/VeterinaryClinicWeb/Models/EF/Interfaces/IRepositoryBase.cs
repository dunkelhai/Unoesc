using VeterinaryClinic.BL;

namespace VeterinaryClinicWeb.Models.EF.Interfaces
{
    public interface IRepositoryBase<T> where T : class, IRegistroBancoDados
    {
        Task Add(T entity);
        Task Delete(T entity);
        Task<IEnumerable<T>> GetAll();
        Task<T> GetById(int id);
        Task Update(T entity);
    }
}
