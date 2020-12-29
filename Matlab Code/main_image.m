D = 'C:\Users\tua_f\Desktop\New folder\dataset2';
A = 'C:\Users\tua_f\Desktop\New folder\Images'
S = dir(fullfile(D,'*'));
K = setdiff({S([S.isdir]).name},{'.','..'}); % list of subfolders of D.
for jj = 1:numel(K)
    fprintf(K{jj});
    fprintf('\n');
    L = dir(fullfile(D,'\',K{jj}));
    N = setdiff({L([L.isdir]).name},{'.','..'}); % list of subfolders of D.
    
    for ii = 1:numel(N)
            fprintf(N{ii});
            fprintf('\n');
            T = dir(fullfile(D,'\',K{jj},'\',N{ii},'*.png')); % improve by specifying the file extension.
            C = {T(~[T.isdir]).name}; % files in subfolder.
            mkdir(fullfile(A,'\',K{jj},'\',N{ii}))
            for ll = 1:numel(C)
                F = fullfile(D,K{jj},N{ii},C{ll})
                % do whatever with file F.
                fusion = main(F)
                %imshow(fusion)
                imwrite(fusion,fullfile(A,'\',K{jj},'\',N{ii},'\',C{ll}))
            end
    end
end

%srcFiles = dir('C:\Users\tua_f\Desktop\New folder\dataset\fish-big\');  % the folder in which ur images exists
%a=dir(['C:\Users\tua_f\Desktop\New folder\dataset\fish-big', '\*.png'])
%out=size(a,1)

%for i = 1:out
   %fusion = main(i)
   %imshow(fusion)
%end

